# coding=UTF-8
import json
from app.module.api import Api
from app.model.areaModel import AreaModel


class AreaControllers(Api, AreaModel):
    def __init__(self):
        Api.__init__(self)
        AreaModel.__init__(self)
        self.currentVersion = "1.0.0"  # 最新版本号

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

    def area1_0_0(self, request):  # 注册 版本1.0.0
        try:
            res = self.getArea()
            return res
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType
