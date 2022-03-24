# coding=UTF-8
import json
import datetime
from app.controllers.login import LoginControllers
from app.controllers.area import AreaControllers
from flask import render_template, Blueprint, request, Response, make_response

loginCont = LoginControllers()
areaCont = AreaControllers()

commApi = Blueprint('commApi', __name__)  # 创建首页路由蓝图


@commApi.route('/login', methods=['POST'])  # 注册api
def apiLoginRoute():
    reqJson = loginCont.run(request, "login")
    user_token = reqJson["user_token"]
    del reqJson['user_token']
    outdate = datetime.datetime.today() + datetime.timedelta(days=30)
    resp = make_response(json.dumps(reqJson))
    resp.set_cookie(
        key='user_token', value=user_token, expires=outdate)
    return resp


@commApi.route('/logup', methods=['POST'])  # 登录api
def apiLogupRoute():
    reqJson = loginCont.run(request, "logup")
    return json.dumps(reqJson)
    # return render_template('register.html')


@commApi.route('/area', methods=['GET'])  # 登录api
def apiAreaRoute():
    reqJson = areaCont.run(request, "area")
    return json.dumps(reqJson)


@commApi.route('/isphone', methods=['POST'])  # 验证手机
def apiPhoneRoute():
    reqJson = loginCont.run(request, "phone")
    return json.dumps(reqJson)
