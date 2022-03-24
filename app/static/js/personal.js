$(function() {
  $.ajax({
    type: "GET",
    url: PATH_API[window.env || "dev"] + "api/user/info",
    dataType: "json",
    success: function(res) {
      if (res.code == 2000) {
        let image = res.data.image,
          name = res.data.name;

        if (image) {
          $(".avatar").attr("src", image);
        }
        $(".user-info strong").text(name);
      } else {
        message(res.msg);
      }
    }
  });
});
