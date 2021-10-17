#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/16 11:18 下午
# @Author   : roninsswang
# @File     : xmlrpc_server.py
# @IDE      : PyCharm
"""
from xmlrpc.server import SimpleXMLRPCServer


class Calculater:
    """
    没有出现url的映射
    没有编码和解码
    序列化和反序列化是xml
    """
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return abs(x - y)

    def divide(self, x, y):
        return x / y


obj = Calculater()
server = SimpleXMLRPCServer(("localhost", 8088))
server.register_instance(obj)  # 将实例注册到rpc server
print("Listening on port 8088...")
server.serve_forever()