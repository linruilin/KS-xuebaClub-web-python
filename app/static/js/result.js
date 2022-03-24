$(function() {
  var ul = $(".table ul").eq(0),
    li_html = "";

  for (let i = 0; 16 > i; i++) {
    li_html += "<li><span>" + i + "</span><span>" + i + "</span></li>";
  }

  ul.append(li_html);
});
