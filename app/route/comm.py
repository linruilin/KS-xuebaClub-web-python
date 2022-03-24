# coding=UTF-8
from flask import render_template, Blueprint, request

# 注册通用错误处理
comm_error = Blueprint('comm_error', __name__)


@comm_error.app_errorhandler(404)
def notFound(err):  # 404 错误
    return render_template('404.html')


@comm_error.app_errorhandler(500)
def serverError(err):  # 500 错误
    return render_template('500.html')


@comm_error.app_errorhandler(502)
def badGateway(err):  # 502 错误
    return render_template('502.html')
