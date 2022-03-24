import pymysql
# from app.module.statusCode import StatusCode
from DBUtils.PooledDB import PooledDB
from config import *


class PTConnectionPool():  # 数据库链接池
    __pool = None

    def __enter__(self):
        self.conn = self.getConn()
        self.cursor = self.conn.cursor()
        return self

    def getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql, host=SQLURL["host"], port=SQLURL["port"],
                                   user=SQLURL["user"], passwd=SQLURL["password"],
                                   db=SQLURL["db"], cursorclass=pymysql.cursors.DictCursor)

        return self.__pool.connection()

    def __exit__(self, type, value, trace):  # 释放连接池资源
        self.cursor.close()
        self.conn.close()


# def getPTConnection():  # 获取PT数据库连接
#     return PTConnectionPool()

getPTConnection = PTConnectionPool()


class MySql():

    # def getconnect(self):  # 链接数据库
    #     self.db = pymysql.connect(host=SQLURL["host"],
    #                               port=SQLURL["port"],
    #                               user=SQLURL["user"],
    #                               password=SQLURL["password"],
    #                               db=SQLURL["db"],
    #                               cursorclass=pymysql.cursors.DictCursor)
        # # 打开数据库连接
        # self.db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

    def getData(self, sql):  # 读取数据
        with getPTConnection as db:
            try:
                # db.cursor.execute(pymysql.escape_string(sql))
                db.cursor.execute(sql)
                resSql = db.cursor.fetchall()
                statusCode = self.get_code("2000")
                statusCode["data"] = resSql
                return statusCode
            except Exception as e:
                statusCode = self.get_code("4000")
                statusCode["error"] = e
                return statusCode

    def postData(self, sql):  # 添加 删除 修改数据操作
        with getPTConnection as db:
            try:
                db.cursor.execute(sql)
                postid = db.cursor.lastrowid
                db.conn.commit()
                statusCode = self.get_code("2000")
                statusCode["data"] = postid
                return statusCode
            except Exception as e:
                db.conn.rollback()
                statusCode = self.get_code("4001")
                statusCode["error"] = e
                return statusCode
        # cursor = self.db.cursor()
        # cursor.execute(sql)
        # # cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
        # # cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)
        # self.db.commit()


# # 执行查询 SQL
# cursor.execute('SELECT * FROM `users`')
# # 获取单条数据
# cursor.fetchone()
# # 获取前N条数据
# cursor.fetchmany(3)
# # 获取所有数据
# cursor.fetchall()
