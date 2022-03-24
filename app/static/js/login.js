var openId = "";

$(function() {
  var code = GetQueryString("code");
  $.ajax({
    type: "POST",
    url: PATH_API[window.env || "dev"] + "api/pay/code",
    data: { code: code },
    dataType: "json",
    success: function(res) {
      if (res.code == 2000) {
        openId = res.data.openid;
      } else {
        message(res.msg);
      }
    }
  });
});

var goRegister = function() {
  window.location.href =
    "/register?openId=" + openId + "&qd=" + GetQueryString("qd");
};

var login = function() {
  var phone = $("#phone").val(),
    password = $("#password").val();

  if (!phone) {
    message("手机号或用户名不能为空");
  } else if (!password) {
    message("密码不能为空");
  } else {
    $.ajax({
      type: "POST",
      url: PATH_API[window.env || "dev"] + "api/login",
      data: { phone: phone, password: password },
      dataType: "json",
      success: function(res) {
        if (res.code == 2000) {
          location.href = "/";
        } else {
          message(res.msg);
        }
      }
    });
  }
};
