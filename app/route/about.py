# coding=UTF-8
import json
from flask import render_template, Blueprint, request, url_for, redirect
from app.module.token import Token
from config import ENV
about = Blueprint('about', __name__)

tokens = Token()


@about.route('/about')  # 注册
def aboutRoute():
    istoken = tokens.valiToken(request)
    if istoken == True:
        return render_template('about.html', ENV=ENV)
    else:
        login_url = url_for('login.loginRoute')
        return redirect(login_url)
