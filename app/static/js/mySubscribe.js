$(function() {
  $.ajax({
    type: "GET",
    url: PATH_API[window.env || "dev"] + "api/user/subscription",
    dataType: "json",
    success: function(res) {
      if (res.code == 2000) {
        var ul = $("#mySubscribe ul").eq(0),
          subscribe_list = res.data,
          ul_html = "";

        subscribe_list.forEach(item => {
          ul_html +=
            "<li><strong class='g-overflow-hidden'>" +
            item.name +
            "</strong><span>" +
            item.money / 100 +
            "元</span></li>";
        });

        ul.append(ul_html);
      } else {
        message(res.msg);
      }
    }
  });
});
