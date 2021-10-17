#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/16 11:26 下午
# @Author   : roninsswang
# @File     : xmlrpc_client.py
# @IDE      : PyCharm
"""

from xmlrpc import client

# xmlrpc client, rpc强调的是本地调用效果
server = client.ServerProxy("http://localhost:8088")
print(server.add(4, 2))
print(server.multiply(4, 2))
print(server.divide(4, 2))
print(server.subtract(2, 4))
