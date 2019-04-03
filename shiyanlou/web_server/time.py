#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: time.py
"
"        Author: xss - callmexss@126.com
"   Description: Show local time
"        Create: 2018-07-02 20:20:17
"""""""""""""""""""""""""""""""""""""""""""""""

from datetime import datetime


print('''\
        <html>
        <body>
        <p>Generated {0}</p>
        </body>
        </html>'''.format(datetime.now()))
