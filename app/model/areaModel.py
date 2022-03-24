# coding=UTF-8
import time
from app.module.mysql import MySql
from app.module.statusCode import StatusCode


class AreaModel(StatusCode, MySql):

    def __init__(self):
        MySql.__init__(self)

    def getArea(self):  # 查询省市区
        try:
            res = self.getData(
                'SELECT area.areaID as id,province,city,area FROM area')
            if res["code"] != "2000":
                statusCode = self.get_code("4000")
            else:
                statusCode = res
            return statusCode
        except Exception as e:
            statusCode = self.get_code("4000")
            return statusCode
