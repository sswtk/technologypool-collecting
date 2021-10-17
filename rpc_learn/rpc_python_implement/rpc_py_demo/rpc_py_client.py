#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/16 10:45 下午
# @Author   : roninsswang
# @File     : rpc_py_client.py
# @Software : PyCharm
"""
import json
import requests


class ClientStub:
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        res = requests.get(f"{self.url}/?a={a}&b={b}")
        return json.loads(res.text).get("res", 0)


client = ClientStub("http://127.0.0.1:8003")
print(client.add(2, 5))
print(client.add(7, 9))
