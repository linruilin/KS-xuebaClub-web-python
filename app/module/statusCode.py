# coding=UTF-8
import json
import copy
from app.module.file import File_txt
from config import STATUS_CODE

file_txt = File_txt()


class StatusCode():  # 代码状态类

    def __init__(self):  # 初始化并加载统一状态码
        try:
            statusCode = file_txt.read_file_str(STATUS_CODE)
            self.statusCode = json.loads(statusCode)
        except Exception as e:
            self.error = {
                "code": "STATUS4001",
                "msg": "状态代码初始化错误",
                "error": str(e)
            }

    def get_code(self, code):
        try:
            statusCode = copy.deepcopy(self.statusCode[str(code)]) 
            return statusCode
        except Exception as e:
            return {
                "code": "STATUS4002",
                "msg": "获取状态代码错误",
                "error": str(e)
            }
