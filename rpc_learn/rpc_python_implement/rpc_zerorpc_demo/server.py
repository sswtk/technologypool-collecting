#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/17 10:03 上午
# @Author   : roninsswang
# @File     : server.py
# @IDE      : PyCharm
"""

import zerorpc


class HelloRPC(object):
    def hello(self, name):
        return "hello, %s" % name


s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()

