#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/17 10:16 上午
# @Author   : roninsswang
# @File     : zero_stream_rpc_server.py
# @IDE      : PyCharm
"""

import zerorpc


class StreamingRPC(object):
    @zerorpc.stream
    def streaming_range(self, fr, to, step):
        return range(fr, to, step)


s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4343")
s.run()