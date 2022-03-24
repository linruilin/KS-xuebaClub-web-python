var requset_status = false;

function pay() {
  if (requset_status) {
    return;
  } else if (getDeviceInfo().browser === "wechat") {
    requset_status = true;
    $.ajax({
      type: "POST",
      url: PATH_API[window.env || "dev"] + "api/pay/order",
      data: {
        openid: GetQueryString("openId"),
        userid: GetQueryString("uid"),
        qd: GetQueryString("qd")
      },
      dataType: "json",
      success: function(res) {
        requset_status = false;
        if (res.code == 2000) {
          if (typeof WeixinJSBridge == "undefined") {
            if (document.addEventListener) {
              document.addEventListener(
                "WeixinJSBridgeReady",
                onBridgeReady,
                false
              );
            } else if (document.attachEvent) {
              document.attachEvent("WeixinJSBridgeReady", onBridgeReady);
              document.attachEvent("onWeixinJSBridgeReady", onBridgeReady);
            }
          } else {
            onBridgeReady(res.data);
          }
        } else {
          message(res.msg);
        }
      }
    });
  }
}

function onBridgeReady(data) {
  WeixinJSBridge.invoke(
    "getBrandWCPayRequest",
    {
      appId: data.appId, //公众号名称，由商户传入
      timeStamp: data.timeStamp, //时间戳，自1970年以来的秒数
      nonceStr: data.nonceStr, //随机串
      package: data.package,
      signType: data.signType, //微信签名方式：
      paySign: data.sign //微信签名
    },
    function(res) {
      if (res.err_msg == "get_brand_wcpay_request:ok") {
        window.location.href = "/login";
      }
    }
  );
}
