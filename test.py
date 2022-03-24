# coding=UTF-8
import unittest
from selenium import webdriver

suite = unittest.TestSuite()  # 创建测试套件
# 找到tests/unit目录下所有的Python文件里面的测试用例
# all_cases = unittest.defaultTestLoader.discover("tests", "*.py")
all_cases = unittest.defaultTestLoader.discover("tests/res", "login.py")

for case in all_cases:
    suite.addTests(case)  # 把所有的测试用例添加进来


def all_unittest():  # 运行所有单元测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    all_unittest()
