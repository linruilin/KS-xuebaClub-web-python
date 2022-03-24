# coding=UTF-8
from config import ENV
import json
from flask import render_template, Blueprint, request, url_for, redirect
from app.module.token import Token
personal = Blueprint('personal', __name__)
tokens = Token()


@personal.route('/personal')  # 我的
def personalRoute():
    istoken = tokens.valiToken(request)
    if istoken == True:
        return render_template('personal.html', ENV=ENV)
    else:
        login_url = url_for('login.loginRoute')
        return redirect(login_url)
