#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time     : 2021/10/16 10:31 下午
# @Author   : roninsswang
# @File     : remote_add.py
# @Software : PyCharm
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl

host = ("", 8003)


class AddHandler(BaseHTTPRequestHandler):
    """
    将url映射到对应的函数，对应到django:urlconfig, 对应到flask:route， 实质是call id的映射
    实现了反序列化
    """
    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = dict(parse_qsl(parsed_url.query))
        a = int(qs.get("a", 0))
        b = int(qs.get("b", 0))
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "res": a + b
        }).encode("utf-8"))


if __name__ == '__main__':
    server = HTTPServer(host, AddHandler)
    print("启动服务器...")
    server.serve_forever()