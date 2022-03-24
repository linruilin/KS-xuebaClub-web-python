# coding=UTF-8
from app.module.file import File_txt
from config import VERSION_TXT

file_txt = File_txt()


class Version():  # 版本号操作类

    def set_version(self):  # 修改版本号
        try:
            # 读取版本文件
            version_txt = file_txt.read_file(VERSION_TXT)
            new_version = ""
            version_length = len(version_txt[0].split("."))
            # 修改版本文件
            for i in version_txt[0].split("."):
                if version_length == 1:
                    version_length = version_length - 1
                    new_version += str(int(i) + 1)
                else:
                    version_length = version_length - 1
                    new_version += i + "."
            # 写入版本号
            file_txt.cover_file(VERSION_TXT, new_version)
        except BaseException as e:
            return {
                "code": "4001",
                "msg": "修改版本号出错",
                "error": str(e)
            }
