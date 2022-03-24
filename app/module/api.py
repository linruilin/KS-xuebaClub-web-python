# coding=UTF-8
from app.module.statusCode import StatusCode
from app.module.validate import Validate

# 不需要验证的接口地址
noPermit = [
    "/api/pay/code",
    "/api/pay/order",
    "/api/pay/callback",
    "/api/area",
    "/api/isphone",
    "/api/login",
    "/api/logup"
]


class Api(StatusCode, Validate):  # api 基类

    def __init__(self):
        StatusCode.__init__(self)
        Validate.__init__(self)

    def run(self, request, name, version="1.0.0"):  # 运行 默认版本号为1.0.0
        try:
            versionType = self.getVersion(name, version)
            validationPermitType = self.validationPermit(request)
            if versionType["code"] != "2000":
                return versionType
            elif validationPermitType["code"] != "2000":
                return validationPermitType
            else:
                return getattr(self, str(versionType["data"]))(request)
        except Exception as e:
            codeType = self.get_code("3001")
            codeType["error"] = e
            return codeType

    def getVersion(self, name, version):  # 版本判断并执行对应版本
        try:
            currentVersion = self.currentVersion.replace(".", "_")
            versions = version.replace(".", "_")
            codeType = self.get_code("2000")
            if hasattr(self, str(name + versions)) == False:
                codeType["data"] = str(name + currentVersion)
                return codeType
            else:
                codeType["data"] = str(name + versions)
                return codeType
        except Exception as e:
            codeType = self.get_code("3002")
            codeType["error"] = e
            return codeType

    def validationPermit(self, request):  # 权限验证
        try:
            permitType = False
            for i in noPermit:
                if str(i) == str(request.path):
                    permitType = True

            if permitType == True:
                codeType = self.get_code("2000")
                return codeType
            else:
                codeType = self.get_code("3003")
                return codeType
        except Exception as e:
            codeType = self.get_code("3003")
            codeType["error"] = e
            return codeType
