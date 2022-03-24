# coding=UTF-8
import time
import datetime
import uuid
import jwt
from flask import Response
from app.module.mysql import MySql
from app.module.statusCode import StatusCode
from app.module.aes import AESCipher
from app.module.statusCode import StatusCode


aes = AESCipher('xuebclub20190901')


class UserModel(StatusCode, MySql):

    def __init__(self):
        MySql.__init__(self)
        StatusCode.__init__(self)

    def postLogin(self, data):  # 登录
        try:
            enc_str = str(aes.encrypt(data["password"]), encoding='utf-8')
            # 查看是否注册
            res = self.getData(
                'SELECT user.userID as id,user.userUUID as uuid,phone FROM user WHERE phone = "%s" and password = "%s" and isOpen = 1' % (
                    data["phone"], enc_str))

            if res["code"] != "2000":
                statusCode = self.get_code("4000")
                return statusCode
            elif len(res["data"]) == 0:
                statusCode = self.get_code("3021")
                return statusCode
            else:
                jwtData = jwt.encode(
                    {'uuid': res["data"][0]["uuid"], 'phone': res["data"][0]["phone"]}, 'secret', algorithm='HS256')
                jwtData = jwtData.decode(encoding='utf-8')
                # 设置token
                statusCode = self.get_code("2000")
                statusCode["user_token"] = jwtData
                return statusCode
        except Exception as e:
            statusCode = self.get_code("4000")
            return statusCode

    def postLogup(self, data):  # 新增注册
        try:
            # 验证是否注册过账户
            res = self.getData(
                'SELECT user.userID as id,phone FROM user WHERE phone = "%s" and isOpen = 1' % (data["phone"]))
            if len(res["data"]) > 0:
                statusCode = self.get_code("3020")
                return statusCode

            enc_str = str(aes.encrypt(data["password"]), encoding='utf-8')

            dateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            userUUID = uuid.uuid1()

            # 写入信息
            resPost = self.postData('INSERT INTO `user` (`userUUID`, `phone`, `password`, `name`, `parentName`, `education`, `parentPhone`, `job`, `address`, `school`, `schoolArea`,`grade`,`className`,`schoolRoll`,`schoolRollArea`,`creation_time`) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", %d, "%s", "%s", "%s", "%s", "%s")' % (
                str(userUUID), str(data["phone"]), enc_str, str(data["name"]), str(data["parentName"]), str(data.get("education", "")), str(data["parentPhone"]), str(data.get("job", "")), str(data["address"]), str(data["school"]), int(data["schoolArea"]), str(data["grade"]), str(data["className"]), str(data["schoolRoll"]), int(data.get("schoolRollArea", "")), str(dateTime)))

            return resPost
        except Exception as e:
            print(e, "error")
            statusCode = self.get_code("4001")
            return statusCode

    def postPhone(self, data):  # 查询手机👌
        try:
            res = self.getData(
                'SELECT user.userID as id,phone FROM user WHERE phone = "%s" and isOpen = 1' % (data["phone"]))

            if res["code"] != "2000":
                statusCode = self.get_code("4000")
                return statusCode
            elif len(res["data"]) > 0:
                statusCode = self.get_code("3020")
                return statusCode
            else:
                statusCode = self.get_code("2000")
                return statusCode
        except Exception as e:
            statusCode = self.get_code("4000")
            return statusCode

    def isLogin(self, data):  # 验证是否登录
        try:
            res = self.getData(
                'SELECT user.userID as id,phone FROM user WHERE userUUID = "%s" and isOpen = 1' % (data["uuid"]))

            if res["code"] != "2000":
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False
        print("UserModel")
