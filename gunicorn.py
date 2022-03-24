# coding=UTF-8
# import multiprocessing

bind = "127.0.0.1:31100"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 2
loglevel = "debug"
accesslog = "./log/gunicorn_access.log"      #访问日志文件
errorlog = "./log/gunicorn_error.log"        #错误日志文件