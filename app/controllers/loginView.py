# coding=UTF-8
import json
import requests
from app.module.api import Api
from app.model.userModel import UserModel
from config import WEIXIN_APP_ID, WEIXIN_MCH_ID, WEIXIN_MCH_KEY, WEIXIN_NOTIFY_URL, WEIXIN_MCH_KEY_FILE, WEIXIN_MCH_CERT_FILE, WEIXIN_APP_SECRET, MONEY


class LoginViewControllers(UserModel):
    def __init__(self):
        UserModel.__init__(self)
        # WeixinUserModel.__init__(self)
        # self.currentVersion = "1.0.0"  # 最新版本号

    def validationData(self, request, name):  # 验证参数 返回验证状态码
        try:
            statusCode = "2000"
            method = request.method
            if method == "get":
                print("getArea")
            else:
                statusCode = "3005"
            return statusCode
        except Exception as e:
            statusCode = "3000"
            return statusCode

    # def login(self, request):  # 登录 版本1.0.0
    #     try:
    #         code = request.args.get("code")
    #         print(code)
    #         data = request.form.to_dict()
    #         print(data)

    #         user_code = request.form.get("code")
    #         url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid="+WEIXIN_APP_ID + \
    #             "&secret="+WEIXIN_APP_SECRET+"&code="+user_code+"&grant_type=authorization_code"
    #         res = requests.get(url)
    #         resjson = json.loads(res.text)
    #         # {'access_token': '25_8IOvXtP8pbSniG7XB2vHo6ZUemm-IE3x27Hu1J_i28skrAJBjjSuto_KIcDlTPYk-4-UAWD8JxsOJ5-b7mi7yQ', 'expires_in': 7200, 'refresh_token': '25_Un886tU6swW0D2jVra-bYj-flbvIKlk0zqcAAlAfZn6m8WeplEcQxH1Ql8Wv1yTp2q7r4YHbHO-6vs9N3DdFkA', 'openid': 'oq5IC1JF2PvQow1H0YzZ09u81DKM', 'scope': 'snsapi_userinfo'}

    #         # userInfoUrl = "https://api.weixin.qq.com/sns/userinfo?access_token=" + \
    #         #     resjson["access_token"]+"&openid=" + \
    #         #     resjson["openid"]+"&lang=zh_CN"
    #         # userRes = requests.get(userInfoUrl)
    #         # userResjson = json.loads(userRes.text)

        except Exception as e:
            print(e)
            # codeType = self.get_code("3001")
            # codeType["error"] = e
            # return codeType
