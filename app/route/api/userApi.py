# coding=UTF-8
import json
import datetime
import time
from app.controllers.user import UserControllers
from flask import render_template, Blueprint, request, Response, make_response

userCont = UserControllers()

userApi = Blueprint('userApi', __name__)  # 创建首页路由蓝图


@userApi.route('/info')  # 获取用户信息
def apiInfoRoute():
    # reqJson = userCont.run(request, "userInfo")
    # print(reqJson, "reqJson")
    reqJson = {
        "code": "2000",
        "msg": "",
        "data": {
            "image": "",
            "name": "学霸"
        }
    }
    return json.dumps(reqJson)

# https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx6e27c1aed0d91117&redirect_uri=http%3a%2f%2fwww.hzfxjy.net%2flogin&response_type=code&scope=snsapi_userinfo#wechat_redirect

# https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx6e27c1aed0d91117&redirect_uri=http%3a%2f%2fwww.hzfxjy.net%2flogin%3fqd%3dweixin&response_type=code&scope=snsapi_userinfo#wechat_redirect


@userApi.route('/subscription')  # 获取用户订阅信息
def apiSsubscriptionRoute():
    # reqJson = payCont.run(request, "getCode")
    reqJson = {
        "code": "2000",
        "msg": "",
        "data": [{
            "money": 128000,
            "name": "求索学霸Club线上服务",
            "time": "20190905084610"
        }]
    }
    return json.dumps(reqJson)
