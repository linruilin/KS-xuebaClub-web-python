# coding=UTF-8
import json
from app.controllers.loginView import LoginViewControllers
from flask import render_template, Blueprint, request
from config import ENV
loginCont = LoginViewControllers()

login = Blueprint('login', __name__)  # 创建首页路由蓝图


@login.route('/login')  # 登录
def loginRoute():
    # loginCont.login(request)
    return render_template('login.html', ENV=ENV)
