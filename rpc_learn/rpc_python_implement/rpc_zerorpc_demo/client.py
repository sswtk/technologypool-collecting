#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/17 10:08 上午
# @Author   : roninsswang
# @File     : client.py
# @IDE      : PyCharm
"""

import zerorpc


c = zerorpc.Client()
c.connect("tcp://0.0.0.0:4242")
print(c.hello("zeroRPC"))
