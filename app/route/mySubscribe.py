# coding=UTF-8
import json
from flask import render_template, Blueprint, request, url_for, redirect
from app.module.token import Token
from config import ENV
mySubscribe = Blueprint('mySubscribe', __name__)

tokens = Token()


@mySubscribe.route('/mySubscribe')  # 注册
def mySubscribeRoute():
    istoken = tokens.valiToken(request)
    if istoken == True:
        return render_template('mySubscribe.html',  ENV=ENV)
    else:
        login_url = url_for('login.loginRoute')
        return redirect(login_url)
