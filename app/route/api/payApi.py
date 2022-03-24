# coding=UTF-8
import json
import datetime
import time
from app.controllers.pay import PayControllers
from flask import render_template, Blueprint, request, Response, make_response

payCont = PayControllers()

payApi = Blueprint('payApi', __name__)  # 创建首页路由蓝图


@payApi.route('/code', methods=['POST'])  # 获取用户信息
def apiCodeRoute():
    reqJson = payCont.run(request, "getCode")
    return json.dumps(reqJson)


@payApi.route('/order', methods=['POST'])  # 下单
def apiOrderRoute():
    reqJson = payCont.run(request, "jsPay")
    return json.dumps(reqJson)


@payApi.route('/callback', methods=['POST'])  # 下单
def apiCallbackRoute():
    reqJson = payCont.run(request, "callback")
    return Response(reqJson, mimetype='text/xml')
    # return str(reqJson)
