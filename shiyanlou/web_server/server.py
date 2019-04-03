#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: server.py
"
"        Author: xss - callmexss@126.com
"   Description: Simple http server
"        Create: 2018-07-02 17:11:20
"""""""""""""""""""""""""""""""""""""""""""""""

from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page = '''\
            <html>
            <body>
            <p>Hello world<p>
            </body>
            </html>
           '''

    # 处理一个HTTP请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
