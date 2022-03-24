# coding=UTF-8
import unittest
import requests
import time
import json
from config import TEST_DOMAIN


class areaApiTest(unittest.TestCase):

    def test_area_get_api(self):  # 获取省市区信息接口
        url = TEST_DOMAIN + '/api/area'
        res = requests.get(url)
        resjson = json.loads(res.text)
        self.assertEqual(200, res.status_code, "获取省市区信息接口请求失败")
        self.assertEqual("2000", resjson["code"], "获取省市区信息接口请求错误")
