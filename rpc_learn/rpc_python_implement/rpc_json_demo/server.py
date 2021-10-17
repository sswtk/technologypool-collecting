#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/16 11:37 下午
# @Author   : roninsswang
# @File     : server.py
# @IDE      : PyCharm
"""

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def add(a, b):
    return a + b


server = SimpleJSONRPCServer(("localhost", 8080))  # 实例化server
server.register_function(add)  # 将函数注册到server中
server.register_function(lambda x, y: x + y, "add")
server.serve_forever()  # 启动server
