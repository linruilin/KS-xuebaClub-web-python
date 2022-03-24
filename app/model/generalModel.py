# coding=UTF-8
import time
import datetime
import uuid
import jwt
from flask import Response
from app.module.mysql import MySql
from app.module.statusCode import StatusCode


class GeneralModel(StatusCode, MySql):

    def __init__(self):
        MySql.__init__(self)

    def postGeneral(self, data):  # 下单
        try:
            # enc_str = str(aes.encrypt(data["password"]), encoding='utf-8')
            dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # 写入订单信息
            res = self.postData('INSERT INTO `general_bill` (`userID`, `money`, `out_trade_no`, `openid`,`creation_time`) VALUES (%d, "%s", "%s", "%s",  "%s")' % (
                int(data["userid"]), int(data["money"]), str(data["order_no"]), str(data["openid"]), str(dateTime)))

            if res["code"] == "2000":
                return res
            else:
                statusCode = self.get_code("4001")
                return statusCode

        except Exception as e:
            statusCode = self.get_code("4001")
            return statusCode
