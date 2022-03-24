# coding=UTF-8

class File_txt():  # txt文件操作类

    def read_file(self, data_path):  # 读文件
        try:
            txt_list = []
            file_txt = open(data_path, 'r', encoding='utf8')
            for line in file_txt.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                if line != "":
                    txt_list.append(line)

            # 关闭文件
            file_txt.close()
            return txt_list
        except BaseException as e:
            return {
                "code": "4001",
                "msg": "读取txt文件错误",
                "error": str(e)
            }

    def read_file_str(self, data_path):  # 读原文件
        try:
            txt_list = ""
            file_txt = open(data_path, 'r', encoding='utf8')
            for line in file_txt.readlines():  # 依次读取每行
                if line != "":
                    txt_list += line

            # 关闭文件
            file_txt.close()
            return txt_list
        except BaseException as e:
            return {
                "code": "4002",
                "msg": "读取原文件错误",
                "error": str(e)
            }

    def write_file(self, data_path, txt):  # 写文件
        try:
            file_txt = open(data_path, mode='a', encoding='utf8')
            file_txt.write(txt)
            # 关闭文件
            file_txt.close()
            return {
                "code": "2000",
                "msg": "写文件成功",
            }
        except BaseException as e:
            return {
                "code": "4003",
                "msg": "写文件错误",
                "error": str(e)
            }

    def cover_file(self, data_path, txt):  # 覆盖写入文件
        try:
            file_txt = open(data_path, mode='w', encoding='utf8')
            file_txt.write(txt)
            # 关闭文件
            file_txt.close()
            return {
                "code": "2000",
                "msg": "覆盖写入文件成功",
            }
        except BaseException as e:
            return {
                "code": "4004",
                "msg": "覆盖写入文件错误",
                "error": str(e)
            }
