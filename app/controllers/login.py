# coding=UTF-8
import json
import requests
from app.module.api import Api
from app.model.userModel import UserModel
from app.module.aes import AESCipher

aes = AESCipher('0987654321qazxcv')


class LoginControllers(Api, UserModel):
    def __init__(self):
        Api.__init__(self)
        UserModel.__init__(self)
        self.currentVersion = "1.0.0"  # 最新版本号

    def validationData(self, request, name):  # 验证参数 返回验证状态码
        try:
            statusCode = "2000"
            method = request.method
            if method == "POST":
                if name == "logup":
                    # * phone 电话 * password 密码 * name 学生姓名
                    # * parentName 家长姓名 education 家长学历
                    # * parentPhone 家长电话 job 家长工作
                    # * address 家庭地址 * school 学校名称
                    # * schoolArea 学校区域 * grade 年级
                    # * className 班级 * schoolRoll 学籍地址
                    # schoolRollArea 学籍区域
                    if request.form.get("phone", False) is False:
                        statusCode = "3006"
                    elif request.form.get("password", False) is False:
                        statusCode = "3007"
                    elif request.form.get("name", False) is False:
                        statusCode = "3008"
                    elif request.form.get("parentName", False) is False:
                        statusCode = "3009"
                    elif request.form.get("parentPhone", False) is False:
                        statusCode = "3010"
                    elif request.form.get("address", False) is False:
                        statusCode = "3011"
                    elif request.form.get("school", False) is False:
                        statusCode = "3012"
                    elif request.form.get("schoolArea", False) is False:
                        statusCode = "3013"
                    elif request.form.get("grade", False) is False:
                        statusCode = "3014"
                    elif request.form.get("className", False) is False:
                        statusCode = "3015"
                    elif request.form.get("schoolRoll", False) is False:
                        statusCode = "3016"
                    elif not self.islength(request.form["phone"], max=30) and not self.isPhone(request.form["phone"]):
                        statusCode = "3017"
                    elif not self.islength(request.form["password"], max=14, min=6) and not self.isPassword(request.form["password"]):
                        statusCode = "3018"
                elif name == "login":
                    if request.form.get("phone", False) is False:
                        statusCode = "3006"
                    elif request.form.get("password", False) is False:
                        statusCode = "3007"
                    elif not self.islength(request.form["phone"], max=30) and not self.isEmail(request.form["phone"]):
                        statusCode = "3017"
                    elif not self.islength(request.form["password"], max=14, min=6) and not self.isPassword(request.form["password"]):
                        statusCode = "3018"
                elif name == "phone":
                    if request.form.get("phone", False) is False:
                        statusCode = "3006"
                    elif not self.islength(request.form["phone"], max=30) and not self.isEmail(request.form["phone"]):
                        statusCode = "3017"
            else:
                statusCode = "3005"
            return statusCode
        except Exception as e:
            statusCode = "3000"
            return statusCode

    def login1_0_0(self, request):  # 登录 版本1.0.0
        try:
            statusCode = self.validationData(request, "login")

            if statusCode == "2000":
                method = request.method
                if method == "POST":
                    data = request.form.to_dict()
                    res = self.postLogin(data)
                    return res
            else:
                codeType = self.get_code(statusCode)
                return codeType
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType

    def logup1_0_0(self, request):  # 注册 版本1.0.0
        try:
            statusCode = self.validationData(request, "logup")

            if statusCode == "2000":
                method = request.method
                if method == "POST":
                    data = request.form.to_dict()

                    enc_str = aes.encrypt(data["phone"])
                    url = 'https://www.xuele.net/trot/member/admin/confirmMobile'
                    res = requests.post(
                        url, data={"key": enc_str.decode('utf8')})

                    resData = json.loads(res.text)
                    if resData["status"] == 1:  # 可以创建小步
                        res = self.postLogup(data)
                        return res
                    else:  # 不可以注册
                        codeType = self.get_code("3019")
                        return codeType
            else:
                codeType = self.get_code(statusCode)
                return codeType
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType

    def phone1_0_0(self, request):  # 验证手机可用 版本1.0.0
        try:
            statusCode = self.validationData(request, "phone")

            if statusCode == "2000":
                method = request.method
                if method == "POST":
                    data = request.form.to_dict()
                    enc_str = aes.encrypt(data["phone"])

                    url = 'https://www.xuele.net/trot/member/admin/confirmMobile'
                    res = requests.post(
                        url, data={"key": enc_str.decode('utf8')})

                    resData = json.loads(res.text)
                    if resData["status"] == 1:  # 可以创建小步
                        reqData = self.postPhone(data)
                        return reqData
                    else:  # 不可以注册
                        codeType = self.get_code("3019")
                        return codeType
            else:
                codeType = self.get_code(statusCode)
                return codeType
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType
