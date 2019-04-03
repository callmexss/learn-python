#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: myfunc.py
"
"        Author: xss - callmexss@126.com
"   Description: My functions
"        Create: 2018-08-13 15:59:07
"""""""""""""""""""""""""""""""""""""""""""""""

import time
import random


def cal_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    print('total time', end - start)


def gen_random(size, start=0, end=100):
    return [random.randint(start, end) for i in range(size)]


def gen_unique_random(size, start=0, end=100):
    res = []
    while len(res) < size:
        num = random.randint(start, end)
        if num not in res:
            res.append(num)
    return res
