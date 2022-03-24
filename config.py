# coding=UTF-8
import os
import platform

# 应用名称
APP_NAME = "KS-xuebaclbe-web-python"

STSTEM_TYPE = platform.system()

# 根目录
ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__))

# 微信配置
WEIXIN_APP_ID = "wx6e27c1aed0d91117"
WEIXIN_APP_SECRET = "9b5eb990b405a3ce84e356c1494c933a"
WEIXIN_MCH_ID = "1552983241"
WEIXIN_MCH_KEY = "13588090097330621199706103792zhu"
# WEIXIN_MCH_KEY = "011c4901e7cdae0c88f984d9ba60829b"
WEIXIN_NOTIFY_URL = "http://www.hzfxjy.net/api/pay/callback"
WEIXIN_MCH_KEY_FILE = ROOT_DIR + "/apiclient_key.pem"
WEIXIN_MCH_CERT_FILE = ROOT_DIR + "/apiclient_cert.pem"

# MONEY = 128000
MONEY = 268000
# MONEY = 1

# 数据库地址
SQLURL = {
    "host": "linruilin.ca4fpmtqnznc.us-west-2.rds.amazonaws.com",
    "port": 3306,
    "user": "linruilin",
    "password": "linruilin31415926",
    "db": 'xueba'
}

# mincached : 启动时开启的闲置连接数量(缺省值 0 以为着开始时不创建连接)
DB_MIN_CACHED = 10

# maxcached : 连接池中允许的闲置的最多连接数量(缺省值 0 代表不闲置连接池大小)
DB_MAX_CACHED = 10

# maxshared : 共享连接数允许的最大数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量,被请求为共享的连接将会被共享使用
DB_MAX_SHARED = 20

# maxconnecyions : 创建连接池的最大数量(缺省值 0 代表不限制)
DB_MAX_CONNECYIONS = 100

# blocking : 设置在连接池达到最大数量时的行为(缺省值 0 或 False 代表返回一个错误<toMany......>; 其他代表阻塞直到连接数减少,连接被分配)
DB_BLOCKING = True

# maxusage : 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用).当达到最大数时,连接会自动重新连接(关闭和重新打开)
DB_MAX_USAGE = 0

# setsession : 一个可选的SQL命令列表用于准备每个会话，如["set datestyle to german", ...]
DB_SET_SESSION = None

# 测试域名
# TEST_DOMAIN = "http://localhost:31100"
TEST_DOMAIN = "http://www.xueba.org"

# 用户版本信息文件
VERSION_TXT = ROOT_DIR + "/version.txt"

# 状态代码文件
STATUS_CODE = ROOT_DIR + "/statusCode.json"

# 开发环境
# ENV = "dev"
# ENV = "test"
# 生产环境
ENV = "produce"
