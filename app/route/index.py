# coding=UTF-8
import json
from flask import render_template, Blueprint, request, url_for, redirect
from app.module.token import Token
from config import ENV
index = Blueprint('index', __name__)  # 创建首页路由蓝图

tokens = Token()

# @index.before_request
# def before_request():
#     log.res_log(request)  # 写入日志


@index.route('/')  # 首页地址
def indexRoute():
    istoken = tokens.valiToken(request)
    if istoken == True:
        return render_template('index.html', ENV=ENV)
    else:
        login_url = url_for('login.loginRoute')
        return redirect(login_url)
