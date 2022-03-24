# coding=UTF-8
import re


class Validate():  # 验证数据类
    def __init__(self):
        self.RegExp = {
            # 防止sql注入
            "string": re.compile(r"insert|select|update|delete|exec|count|'|\"|=|;|>|<|%", re.I),
            # 防止sql注入 内容
            "contentString": re.compile(r"'|\"|=|;|>|<|%", re.I),
            # 非零整数
            "PositiveInteger": re.compile(r"^[0-9]*[1-9][0-9]*$"),
            # 密码验证
            "Password": re.compile(r"^[a-zA-Z0-9!@#$]{6,14}$"),
            # 中国手机号码验证
            "Phone": re.compile(r"^1[3|4|5|7|8][0-9]\d{4,8}$"),
            # 邮箱验证
            "Email": re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"),
        }

    def islength(self, value, **length):  # 验证长度是否正确 max 为最大长度 min 为最小长度
        try:
            lengthType = False
            value_Len = len(value)
            len_Max = length.get("max")
            len_Min = length.get("min")
            if not len_Max is None and not len_Min is None:
                if value_Len <= len_Max and value_Len >= len_Min:
                    lengthType = True
            elif not len_Max is None:
                if value_Len <= len_Max:
                    lengthType = True
            elif not len_Min is None:
                if value_Len >= len_Min:
                    lengthType = True

            return lengthType
        except Exception as e:
            return False

    def isPassword(self, value):  # 验证密码格式是否正确
        try:
            if len(value) == re.search(self.RegExp["Password"], value).span()[1]:
                return True
            else:
                return False
        except Exception:
            return False

    def isEmail(self, value):  # 验证邮箱地址是否正确
        try:
            if len(value) == re.search(self.RegExp["Email"], value).span()[1]:
                return True
            else:
                return False
        except Exception:
            return False
    
    def isPhone(self, value):  # 验证电话号码
        try:
            if len(value) == re.search(self.RegExp["Phone"], value).span()[1]:
                return True
            else:
                return False
        except Exception:
            return False
