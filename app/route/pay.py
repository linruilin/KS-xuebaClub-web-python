# coding=UTF-8
import json
from flask import render_template, Blueprint, request
from config import ENV
pay = Blueprint('pay', __name__)


@pay.route('/pay/way')  # 注册
def payRoute():
    return render_template('pay.html',  ENV=ENV)
