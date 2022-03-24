#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.web import main

app = main()
# manager = Manager(app)

# print(app.url_map, "路由列表")

# 添加程序运行
def qsweb():
    # manager.run()
    app.run()

if __name__ == "__main__":
    qsweb()