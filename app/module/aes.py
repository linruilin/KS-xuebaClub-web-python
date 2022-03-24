# coding=UTF-8
import base64
import json
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AESCipher:  # AES/CBC/加密

    def __init__(self, key):
        self.bs = 16
        self.key = key[0:16].encode("utf8")  # 只截取16位
        # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求。
        self.iv = "0102030405060708".encode("utf8")
        self.__pad = lambda s: s + (self.bs - len(s.encode("utf8")) %
                                    self.bs) * chr(self.bs - (len(s.encode("utf8"))) % self.bs)
        self.__unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, raw):  # 加密
        raw = self.__pad(raw)
        # print(raw, "raw", len(raw))
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))
        # return b2a_hex(cipher.encrypt(raw))
        # return base64.urlsafe_b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):  # 解密
        enc = base64.b64decode(enc)
        # enc = base64.urlsafe_b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # print((str(cipher.decrypt(enc), encoding='utf-8'), 111111))
        return self.__unpad(str(cipher.decrypt(enc), encoding='utf-8'))
