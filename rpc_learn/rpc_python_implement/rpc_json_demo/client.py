#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/16 11:38 下午
# @Author   : roninsswang
# @File     : client.py
# @IDE      : PyCharm
"""
import threading
import time

import jsonrpclib

print(jsonrpclib.config.version)

def req():
    server = jsonrpclib.jsonrpc.ServerProxy("http://localhost:8080")
    print(server.add(2, 5))


for i in range(10):
    thread = threading.Thread(target=req)
    thread.start()

time.sleep(30)