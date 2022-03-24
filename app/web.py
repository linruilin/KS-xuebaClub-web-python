# coding=UTF-8
from flask import Flask
from config import ENV
import time
from weixin import Weixin, WeixinError
from app.module.version import Version
from app.route.index import index
from app.route.login import login
from app.route.register import register
from app.route.personal import personal
from app.route.pay import pay
from app.route.about import about
from app.route.mySubscribe import mySubscribe
from app.route.api.commApi import commApi
from app.route.api.payApi import payApi
from app.route.api.userApi import userApi
from app.route.comm import comm_error


version = Version()

app = Flask(__name__, static_url_path='')
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(register, url_prefix='/')
app.register_blueprint(personal, url_prefix='/')
app.register_blueprint(pay, url_prefix='/')
app.register_blueprint(about, url_prefix='/')
app.register_blueprint(mySubscribe, url_prefix='/')
app.register_blueprint(commApi, url_prefix='/api')
app.register_blueprint(payApi, url_prefix='/api/pay')
app.register_blueprint(userApi, url_prefix='/api/user')
# app.register_blueprint(comm_error)

config = dict(WEIXIN_APP_ID='', WEIXIN_APP_SECRET='')
weixin = Weixin(config)


def main():  # 输入app程序
    if ENV == "dev":  # 判断开发环境
        version.set_version()
    return app
