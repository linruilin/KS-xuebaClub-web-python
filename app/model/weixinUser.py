# coding=UTF-8
import time
import datetime
import uuid
import jwt
from flask import Response
from app.module.mysql import MySql
from app.module.statusCode import StatusCode
from app.module.aes import AESCipher


aes = AESCipher('xuebclub20190901')


class WeixinUserModel(StatusCode, MySql):

    def __init__(self):
        MySql.__init__(self)
        StatusCode.__init__(self)

    def postWeixinUser(self, data):  # 新增微信OpenId
        try:
            # {'access_token': '25_8IOvXtP8pbSniG7XB2vHo6ZUemm-IE3x27Hu1J_i28skrAJBjjSuto_KIcDlTPYk-4-UAWD8JxsOJ5-b7mi7yQ', 'expires_in': 7200, 'refresh_token': '25_Un886tU6swW0D2jVra-bYj-flbvIKlk0zqcAAlAfZn6m8WeplEcQxH1Ql8Wv1yTp2q7r4YHbHO-6vs9N3DdFkA', 'openid': 'oq5IC1JF2PvQow1H0YzZ09u81DKM', 'scope': 'snsapi_userinfo'}
            # 写入信息
            resPost = self.postData(
                'INSERT INTO `weixinUser` (`openid`) VALUES ("%s")' % (str(data["openid"])))
            return resPost
        except Exception as e:
            print(e, "error")
            statusCode = self.get_code("4001")
            return statusCode
