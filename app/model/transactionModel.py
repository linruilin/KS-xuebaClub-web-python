# coding=UTF-8
import time
import datetime
import uuid
import jwt
import json
import requests
from flask import Response
from app.module.mysql import MySql
from app.module.statusCode import StatusCode
from app.module.aes import AESCipher


aes = AESCipher('0987654321qazxcv')


class TransactionModel(StatusCode, MySql):

    def __init__(self):
        MySql.__init__(self)

    def postTransaction(self, data):  # 下单
        try:

             # <xml>
            #     <appid><![CDATA[wx6e27c1aed0d91117]]></appid>
            #     <attach><![CDATA[学霸注册74]]></attach>
            #     <bank_type><![CDATA[CFT]]></bank_type>
            #     <cash_fee><![CDATA[1]]></cash_fee>
            #     <fee_type><![CDATA[CNY]]></fee_type>
            #     <is_subscribe><![CDATA[Y]]></is_subscribe>
            #     <mch_id><![CDATA[1552983241]]></mch_id>
            #     <nonce_str><![CDATA[62EbRzo4aLgRLdy4HWCIzwQ55V5NW8lS]]></nonce_str>
            #     <openid><![CDATA[oq5IC1JF2PvQow1H0YzZ09u81DKM]]></openid>
            #     <out_trade_no><![CDATA[201909050621533784769]]></out_trade_no>
            #     <result_code><![CDATA[SUCCESS]]></result_code>
            #     <return_code><![CDATA[SUCCESS]]></return_code>
            #     <sign><![CDATA[1DBD772B35D22E145194BD000F1EF994]]></sign>
            #     <time_end><![CDATA[20190905062158]]></time_end>
            #     <total_fee>1</total_fee>
            #     <trade_type><![CDATA[JSAPI]]></trade_type>
            #     <transaction_id><![CDATA[4200000385201909055342743998]]></transaction_id>
            # </xml>

            # data = {
            #     "cash_fee": tree.find("cash_fee").text,
            #     "fee_type": tree.find("fee_type").text,
            #     "openid": tree.find("openid").text,
            #     "out_trade_no": tree.find("out_trade_no").text,
            #     "result_code": tree.find("result_code").text,
            #     "time_end": tree.find("time_end").text,
            #     "total_fee": tree.find("total_fee").text,
            #     "transaction_id": tree.find("transaction_id").text
            # }
            res = {}
            print(data["result_code"], 'data["result_code"]')
            if data["result_code"] == "SUCCESS":

                # 写入订单信息
                res = self.postData('INSERT INTO `transaction_bill` (`method`, `payable`, `actualPayment`,`fee_type`,`payType`,`transaction_id`,`out_trade_no`,`pay_end_time`,`openid`) VALUES ("%s", %d, %d, "%s",  %d,"%s", "%s", "%s", "%s")' % (
                    "微信支付", int(data["total_fee"]), int(data["cash_fee"]), str(data["fee_type"]), 1, str(data["transaction_id"]), str(data["out_trade_no"]), str(data["time_end"]), str(data["openid"])))

                if res["code"] != "2000":
                    statusCode = self.get_code("4001")
                    return statusCode

                getUser = self.getData(
                    'SELECT * FROM (transaction_bill as trans LEFT JOIN general_bill as gen ON trans.out_trade_no = gen.out_trade_no) LEFT JOIN user as user ON gen.userID = user.userID WHERE trans.out_trade_no="%s"' % (str(data["out_trade_no"])))

                if getUser["code"] != "2000":
                    statusCode = self.get_code("4001")
                    return statusCode

                update = self.postData(
                    'UPDATE user SET isOpen = 1,openid = "%s" WHERE userID = %d' % (data["openid"], getUser["data"][0]["userID"]))

                if update["code"] != "2000":
                    statusCode = self.get_code("4001")
                    return statusCode

                # 注册小步智学
                xiaobuData = {"mobile": str(getUser["data"][0]["phone"]), "name": str(getUser["data"][0]["name"]), "school": str(
                    getUser["data"][0]["school"]), "className": str(getUser["data"][0]["className"]), "homeAdd": str(getUser["data"][0]["address"]), "grade": "6"}
                xiaobuData = json.dumps(xiaobuData, ensure_ascii=False)
                print(xiaobuData)
                enc_str = aes.encrypt(xiaobuData)
                print(enc_str.decode('utf8'))
                url = 'https://www.xuele.net/trot/order/createStudentByWasu'
                res = requests.post(
                    url, data={"key": enc_str.decode('utf8')})
                print(res.text, "注册小步账户")
                resData = json.loads(res.text)

                if resData["status"] == 1:  # 创建小步账户
                    codeType = self.get_code("2000")
                    # reqData = self.postPhone(data)
                    return codeType
                else:  # 不可以注册
                    codeType = self.get_code("2000")
                    # reqData = self.postPhone(data)
                    return codeType

                # json.dumps(secret_data, ensure_ascii=False)
            else:
                print("支付失败", data)
                res = self.postData('INSERT INTO `transaction_bill` (`method`, `payable`, `actualPayment`,`fee_type`,`payType`,`transaction_id`,`out_trade_no`,`pay_end_time`,`openid`) VALUES ("%s", %d, %d, "%s", %d,"%s", "%s", "%s", "%s")' % (
                    "微信支付", int(data["total_fee"]), int(data["cash_fee"]), str(data["fee_type"]), 0, str(data["transaction_id"]), str(data["out_trade_no"]), str(data["time_end"]), str(data["openid"])))

            if res["code"] == "2000":
                return res
            else:
                statusCode = self.get_code("4001")
                return statusCode

            # if res["code"] != "2000":
            #     statusCode = self.get_code("4000")
            #     return statusCode
            # elif len(res["data"]) == 0:
            #     statusCode = self.get_code("3021")
            #     return statusCode
            # else:
            #     jwtData = jwt.encode(
            #         {'uuid': res["data"][0]["uuid"], 'phone': res["data"][0]["phone"]}, 'secret', algorithm='HS256')
            #     jwtData = jwtData.decode(encoding='utf-8')
            #     # 设置token
            #     statusCode = self.get_code("2000")
            #     statusCode["user_token"] = jwtData
            #     return statusCode
        except Exception as e:
            print(e, "微信回调错误")
            statusCode = self.get_code("4001")
            return statusCode
