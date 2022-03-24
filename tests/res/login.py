# coding=UTF-8
import unittest
import requests
import time
import json
from config import TEST_DOMAIN


class LoginApiTest(unittest.TestCase):

    # def test_phone_post_api(self):  # 验证手机号
    #     url = TEST_DOMAIN + '/api/isphone'

    #     res = requests.post(url, data={'phone': '18814885423'})
    #     resjson = json.loads(res.text)
    #     # print(resjson, "resjson")
    #     self.assertEqual(200, res.status_code, "验证手机号接口请求失败")
    #     self.assertEqual("2000", resjson["code"], "验证手机号接口请求错误")

    #     res2 = requests.post(url, data={'phone': '18042303080'})
    #     resjson2 = json.loads(res2.text)
    #     # print(resjson2, "resjson2")
    #     self.assertEqual(200, res2.status_code, "验证手机号接口请求失败")

    # def test_login_post_api(self):  # 登录API测试
    #     url = TEST_DOMAIN + '/api/login'
    #     data = {
    #         "phone": "18042303080",
    #         "password": "123456",
    #     }
    #     res = requests.post(url, data=data)
    #     # print(res.cookies['user_token'])
    #     # # print(res.cookies['user_token'], "user_token")
    #     # print(res.text)
    #     resjson = json.loads(res.text)
    #     print(resjson)
    #     self.assertEqual(200, res.status_code, "登录接口请求失败")
    #     self.assertEqual("2000", resjson["code"], "登录接口请求错误")

    def test_logup_post_api(self):  # 注册API测试
        url = TEST_DOMAIN + '/api/logup'
        # * phone 电话 * password 密码 * name 学生姓名
        # * parentName 家长姓名 education 家长学历
        # * parentPhone 家长电话 job 家长工作
        # * address 家庭地址 * school 学校名称
        # * schoolArea 学校区域 * grade 年级
        # * className 班级 * schoolRoll 学籍地址
        # schoolRollArea 学籍区域
        data = {
            "phone": "18042303081",
            "password": "123456",
            "name": "test",
            "parentName": "parentName",
            # "education": "education",
            "parentPhone": "18814885423",
            # "job": "job",
            "address": "address",
            "school": "school",
            "schoolArea": 1,
            "grade": "grade",
            "className": "className",
            "schoolRoll": "schoolRoll",
            "schoolRollArea": 1,
            # "schoolRollArea": "",
        }
        print(1111)
        res = requests.post(url, data=data)
        resjson = json.loads(res.text)
        # print(resjson)
        self.assertEqual(200, res.status_code, "注册接口请求失败")
        self.assertEqual("2000", resjson["code"], "注册接口请求错误")
