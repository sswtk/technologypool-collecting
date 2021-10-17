#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/17 10:20 上午
# @Author   : roninsswang
# @File     : zero_stream_rpc_client.py
# @IDE      : PyCharm
"""


import zerorpc


c = zerorpc.Client()
c.connect("tcp://0.0.0.0:4343")

for i in c.streaming_range(10, 20, 2):
    print(i)