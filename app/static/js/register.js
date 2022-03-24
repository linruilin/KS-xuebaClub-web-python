var LAreaData = [],
  requset_status = false;
var submit_param = [
  {
    key: "phone",
    must: true
  },
  {
    key: "password",
    must: true
  },
  {
    key: "again_password",
    must: true
  },
  {
    key: "name",
    must: true
  },
  {
    key: "parentName",
    must: true
  },
  {
    key: "education",
    must: false
  },
  {
    key: "parentPhone",
    must: true
  },
  {
    key: "job",
    must: false
  },
  {
    key: "address",
    must: true
  },
  {
    key: "school",
    must: true
  },
  {
    key: "schoolArea",
    must: true
  },
  {
    key: "grade",
    must: true
  },
  {
    key: "className",
    must: true
  },
  {
    key: "schoolRoll",
    must: true
  },
  {
    key: "schoolRollArea",
    must: false
  }
];

$(function() {
  $.ajax({
    type: "GET",
    url: PATH_API[window.env || "dev"] + "api/area",
    dataType: "json",
    success: function(res) {
      if (res.code == 2000) {
        var citys = {};

        res.data.forEach(function(item) {
          var param = {
            id: item.id,
            name: item.area
          };

          if (!citys[item.province]) {
            citys[item.province] = {
              [item.city]: [param]
            };
          } else if (!citys[item.province][item.city]) {
            citys[item.province][item.city] = param;
          } else {
            citys[item.province][item.city].push(param);
          }
        });

        var index = 0;
        for (var i in citys) {
          LAreaData.push({ name: i, child: [] });
          for (var j in citys[i]) {
            LAreaData[index].child.push({
              name: j,
              child: citys[i][j]
            });
          }
          index++;
        }

        ["schoolArea", "schoolRollArea"].forEach(function(item) {
          var area = new LArea();

          area.init({
            trigger: "." + item + "_name", //触发选择控件的文本框，同时选择完毕后name属性输出到该位置
            valueTo: "." + item, //选择完毕后id属性输出到该位置
            keys: { id: "id", name: "name" }, //绑定数据源相关字段 id对应valueTo的value属性输出 name对应trigger的value属性输出
            type: 1, //数据源类型
            data: LAreaData //数据源
          });
        });
      } else {
        message(res.msg);
      }
    }
  });

  // 协议选择
  $(".treaty-select").click(function() {
    var state = $(this).hasClass("active");

    if (state) {
      $(this).removeClass("active");
    } else {
      $(".popup").show();
    }
  });
});

var operate = function(type) {
  $(".popup").hide();

  if (type === "confirm") {
    $(".treaty-select").addClass("active");
  }
};

var isphone = function() {
  var phone = $(".phone").val();

  if (!phone) {
    message("手机号码不能为空");
  } else {
    $.ajax({
      type: "POST",
      url: PATH_API[window.env || "dev"] + "api/isphone",
      data: {
        phone: phone
      },
      dataType: "json",
      success: function(res) {
        message(res.code == 2000 ? "该手机未尚未注册" : res.msg);
      }
    });
  }
};

var register = function() {
  if (requset_status) {
    return;
  } else if (!$(".treaty-select").hasClass("active")) {
    message("请先勾选应用协议");
    return;
  }

  var param = {};

  for (var i = 0; submit_param.length > i; i++) {
    var key = submit_param[i].key,
      value = $("." + key).val();

    if (submit_param[i].must && !value) {
      message($("." + key)[0].placeholder);
      $("." + key).focus();
      return;
    } else {
      if (key === "again_password" && value != $(".password").val()) {
        message("密码不一致");
        $("." + key).focus();
        return;
      } else {
        if (value)
          param[key] =
            key === "schoolArea" || key === "schoolRollArea"
              ? value.split(",")[2]
              : value;
      }
    }
  }

  requset_status = true;
  $.ajax({
    type: "POST",
    url: PATH_API[window.env || "dev"] + "api/logup",
    data: param,
    dataType: "json",
    success: function(res) {
      requset_status = false;
      if (res.code == 2000) {
        window.location.href =
          "/pay/way?openId=" +
          GetQueryString("openId") +
          "&uid=" +
          res.data +
          "&qd=" +
          GetQueryString("qd");
      } else {
        message(res.msg);
      }
    }
  });
};
