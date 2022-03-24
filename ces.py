# coding=UTF-8
import base64
import json
import urllib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


from app.module.aes import AESCipher

aes = AESCipher('0987654321qazxcv')


BS = AES.block_size

def pad(s): return s + (BS - len(s.encode("utf8")) %
                        BS) * chr(BS - len(s.encode("utf8")) % BS)


def unpad(s): return s[0:-ord(s[-1])]


def unpad2(text):
    length = len(text)
    unpadding = ord(text[len(text)-1])
    return text[0:length-unpadding]
    # print(s,333333333)
    # print(s[-1])
    # print(ord(s[-1]))
    # return s[0:-ord(s[-1])]


# class AESCipher:  # AES/CBC/加密

#     def __init__(self, key):
#         self.bs = 16
#         self.key = key[0:16].encode("utf8")  # 只截取16位
#         # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求。
#         self.iv = "0102030405060708".encode("utf8")
#         self.__pad = lambda s: s + (self.bs - len(s.encode("utf8")) %
#                                     self.bs) * chr(self.bs - (len(s.encode("utf8"))) % self.bs)
#         self.__unpad = lambda s: s[0:-ord(s[-1])]

#     def encrypt(self, raw):  # 加密
#         raw = self.__pad(raw)
#         # print(raw, "raw", len(raw))
#         cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
#         return base64.b64encode(cipher.encrypt(raw))
#         # return b2a_hex(cipher.encrypt(raw))
#         # return base64.urlsafe_b64encode(cipher.encrypt(raw))

#     def decrypt(self, enc):  # 解密
#         enc = base64.b64decode(enc)
#         # enc = base64.urlsafe_b64decode(enc)
#         cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
#         print(cipher.decrypt(enc), 111111)
#         return self.__unpad(cipher.decrypt(enc))


if __name__ == '__main__':
    e = AESCipher('0987654321qazxcv')
    # secret_data = "18042303080    华数学院班测试"
    secret_data = {'mobile': '18042303080', 'name': '林睿霖', 'school': '我们的', 'homeAdd': '我们的', 'grade': '6'}
    secret_data = (json.dumps(secret_data, ensure_ascii=False))
    print(secret_data)
    # secret_data = {"mobile": "15812121212", "name": "测试",
    #                "school": "华数学院", "className": "1班", "homeAdd": "华数", "grade": "1"}
    # secret_data2 = '{"mobile":"15812121212","name":"测试","school":"华数学院","className":"1班","homeAdd":"华数","grade":1}'
    # # secret_data2 = '1111'
    # secret_data3 = str({"mobile": "15812121212", "name": "测试",
    #                     "school": "华数学院", "className": "1班", "homeAdd": "华数", "grade": "1"})

    # print(secret_data2, "secret_data2")
    # print(json.dumps(secret_data, ensure_ascii=False), "secret_data")
    # enc_str = e.encrypt(json.dumps(secret_data, ensure_ascii=False))
    enc_str = e.encrypt(secret_data)
    
#
    print(enc_str.decode())
    
    # if enc_str.decode() == "NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIpo81WYwPEozdoZ63aIce46OJ91n4fNSmDMhBdXQ3vtg":
    #     print('enc_str: ' + enc_str.decode())
    # else:
    #     #         NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIJRz9BlMH7xkanBm4WXoaiA==
    #     # NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIpo81WYwPEozdoZ63aIce46OJ91n4fNSmDMhBdXQ3vtg
    #     # NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIJRz9BlMH7xkanBm4WXoaiGY-8bOX2JeDe0COY4ZUobo=
    #     # NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIpo81WYwPEozdoZ63aIce46OJ91n4fNSmDMhBdXQ3vtg
    #     print("不对称")
    #     print(enc_str.decode())
    #     print("NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIpo81WYwPEozdoZ63aIce46OJ91n4fNSmDMhBdXQ3vtg")

    # dec_str = e.decrypt(enc_str.decode())
    # print('dec str: ' + dec_str)

    # text = 'NWnZolaTfsIRfF19CRsu9l7J77C3oPKS90oVQ4aK0ZdE1jGGPQbxpTHBQe2t6VJfUSN0KyAAb6PYzgmZwijHO48a5mS49TZpUnT1wQhu4HLVow-5wuSAVwFvXL-cRVwIpo81WYwPEozdoZ63aIce46OJ91n4fNSmDMhBdXQ3vtg'

    # dec_str2 = e.decrypt(text.encode())
    # print('dec str: ' + dec_str2)

    # enc1 = base64.b64encode(secret_data2.encode())
    # print(enc1.decode("utf-8"), "enc1")
    # enc2 = base64.urlsafe_b64encode(secret_data2.encode())
    # print(enc2.decode("utf-8"), "enc2")

    # dec1 = base64.b64decode(enc1)
    # print(dec1, "dec1")
    # dec2 = base64.urlsafe_b64decode(enc2)
    # print(dec2, "dec2")
