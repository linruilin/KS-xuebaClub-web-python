# coding=UTF-8
import unittest
import requests
import time
import json
from config import TEST_DOMAIN


class PayApiTest(unittest.TestCase):

    def test_info_post_api(self):  # 用户信息
        url = TEST_DOMAIN + '/api/user/info'
        res = requests.get(url)
        resjson = json.loads(res.text)
        print(resjson,"resjson")
        self.assertEqual(200, res.status_code, "获取code接口请求失败")
        self.assertEqual("2000", resjson["code"], "获取code接口请求错误")

    def test_subscription_post_api(self):  # 用户订阅
        url = TEST_DOMAIN + '/api/user/subscription'
        res = requests.get(url)
        resjson = json.loads(res.text)
        self.assertEqual(200, res.status_code, "调用api支付接口请求失败")
        self.assertEqual("2000", resjson["code"], "调用api支付接口请求错误")
