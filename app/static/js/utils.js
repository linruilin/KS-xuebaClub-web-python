document.documentElement.style.fontSize =
  document.documentElement.clientWidth / 7.5 + "px";

/**
 * 获取设备信息
 * @return {Object}
 */
var getDeviceInfo = function() {
  let u = navigator.userAgent,
    device = {
      isMobile: /(iPhone|iPad|iPod|iOS|Android|Linux)/i.test(u),
      browser:
        u.indexOf("MicroMessenger") !== -1
          ? "wechat"
          : u.indexOf("QQ") !== -1
          ? "qq"
          : "else",
      system:
        u.indexOf("Android") > -1 || u.indexOf("Linux") > -1 ? "Android" : "ios"
    };

  return device;
};

var message = function(text) {
  $("body").append('<span id="g-message">' + text + "</span>");

  setTimeout(function() {
    $("#g-message").remove();
  }, 2000);
};

/**
 * api 地址
 * 环境 {
 *    dev - 开发
 *    test - 测试
 *    master - 线上
 * }
 */
var PATH_API = {
  dev: "http://127.0.0.1:5000/",
  test: "http://www.hzfxjy.net/",
  produce: "http://www.hzfxjy.net/"
};

var GetQueryString = function(name) {
  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
  var r = window.location.search.substr(1).match(reg);
  if (r != null) return unescape(r[2]);
  return null;
};
