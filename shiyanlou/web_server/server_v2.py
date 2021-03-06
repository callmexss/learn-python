#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: server.py
"
"        Author: xss - callmexss@126.com
"   Description: Simple http server
"        Create: 2018-07-02 17:11:20
"""""""""""""""""""""""""""""""""""""""""""""""
import os
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerException(Exception):
    '''服务器内部错误'''
    pass


class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    Error_Page = '''\
            <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            <p></p>
            </body>
            </html>
            '''

    def do_GET(self):
        try:

            full_path = os.getcwd() + self.path

            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            else:
                raise ServerException("Unknown object '{0}'".format(self.path))

        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode('utf-8'), 404)

    def send_content(self, page, statue=200):
        self.send_response(statue)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
