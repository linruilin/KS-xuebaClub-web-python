# coding=UTF-8
import json
from flask import render_template, Blueprint, request
from config import ENV
register = Blueprint('register', __name__)


@register.route('/register')  # 注册
def registerRoute():
    return render_template('register.html', ENV=ENV)
