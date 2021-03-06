#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: server.py
"
"        Author: xss - callmexss@126.com
"   Description: Simple http server 3.0
"        Create: 2018-07-02 17:11:20
"""""""""""""""""""""""""""""""""""""""""""""""
import os
import subprocess

from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerException(Exception):
    '''服务器内部错误'''
    pass


class case_no_file(object):
    '''路径不存在'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0} not found".format(handler.path))


class case_existing_file(object):
    '''路径是文件'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)


class case_always_fail(object):
    '''所有情况都不符合时的默认处理类'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))


class case_directory_index_file(object):
    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))

    def act(self, handler):
        handler.handle_file(self.index_path(handler))


class case_cgi_file(object):
    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('py')

    def act(self, handler):
        handler.run_cgi(handler.full_path)


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
    Cases = [case_no_file(),
             case_cgi_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_always_fail()]

    def do_GET(self):
        try:

            self.full_path = os.getcwd() + self.path

            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break

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

    def run_cgi(self, full_path):
        data = subprocess.check_output(['python3', full_path], shell=False)
        self.send_content(data)

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
