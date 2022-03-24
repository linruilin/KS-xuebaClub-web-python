$(function() {
  var list = [
      {
        id: 1,
        video_img:
          "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564486582300&di=f7bc5ac865ad35821d5abaccd2669a4b&imgtype=0&src=http%3A%2F%2Fg.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F5366d0160924ab18014cefd83bfae6cd7a890b82.jpg",
        title: "课程名称--换种方式去旅行·最美的记忆永远在远方",
        content:
          "如果在暮春的烟雨中抚琴一曲，并在脸颊露着不易察觉的浅笑，那么，在荷花初绽的时节一定会遇到惊喜 ，此时音乐的旋律将是高山流水般的ds ，此时音乐的旋律将是高山流水般的"
      },
      {
        id: 2,
        video_img:
          "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564486582300&di=f7bc5ac865ad35821d5abaccd2669a4b&imgtype=0&src=http%3A%2F%2Fg.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F5366d0160924ab18014cefd83bfae6cd7a890b82.jpg",
        title: "课程名称--换种方式去旅行·最美的记忆永远在远方",
        content:
          "如果在暮春的烟雨中抚琴一曲，并在脸颊露着不易察觉的浅笑，那么，在荷花初绽的时节一定会遇到惊喜 ，此时音乐的旋律将是高山流水般的ds ，此时音乐的旋律将是高山流水般的"
      }
    ],
    html = "";

  list.forEach(function(item) {
    html +=
      "<a class='li' href='./curriculumDetail.html?id=" +
      item.id +
      "'><div class='video-img'><img src='" +
      item.video_img +
      "' alt /></div><strong class='g-overflow-hidden'>" +
      item.title +
      "</strong><span>" +
      item.content +
      "</span></a>";
  });

  $("#curriculum").append(html);
});
