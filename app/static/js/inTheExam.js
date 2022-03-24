$(function() {
  countdown(88);
});

var countdown = function(val) {
  var minute = parseInt(val / 60),
    second = val % 60,
    str = minute + "分" + second + "秒";

  $("header strong").html(str);

  setTimeout(function() {
    if (val === 0) {
      return;
    }
    countdown(--val);
  }, 1000);
};
