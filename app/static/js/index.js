var goAPP = function () {
  var system = getDeviceInfo().system;

  if (system === "ios") {
    location.href = "http://m.xuele.net/";
  } else {
    location.href =
      "https://sj.qq.com/myapp/detail.htm?apkName=net.xuele.xuelec2";
  }
};