# coding=UTF-8
import unittest
import requests
import time
import json
from config import TEST_DOMAIN


class PayApiTest(unittest.TestCase):

    def test_code_post_api(self):  # 用户授权
        url = TEST_DOMAIN + '/api/pay/code'
        res = requests.post(
            url, data={'code': '001sJt3T0LO7QZ1RWb1T0Bmx3T0sJt3B'})
        resjson = json.loads(res.text)
        self.assertEqual(200, res.status_code, "获取code接口请求失败")
        self.assertEqual("2000", resjson["code"], "获取code接口请求错误")

    def test_jsPay_post_api(self):  # 调用api支付
        url = TEST_DOMAIN + '/api/pay/order'
        res = requests.post(
            url, data={'openid': 'oq5IC1JF2PvQow1H0YzZ09u81DKM', 'userid': '10'})
        resjson = json.loads(res.text)
        self.assertEqual(200, res.status_code, "调用api支付接口请求失败")
        self.assertEqual("2000", resjson["code"], "调用api支付接口请求错误")

    def test_callback_post_api(self):  # 调用api支付
        url = TEST_DOMAIN + '/api/pay/callback'
        res = requests.post(url)
        print(res.text,"text")
        # resjson = json.loads(res.text)
        # print(resjson, "test")
        # self.assertEqual(200, res.status_code, "调用api支付接口请求失败")
        # self.assertEqual("2000", resjson["code"], "调用api支付接口请求错误")
