#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: test_sample.py
"
"        Author: xss - callmexss@126.com
"   Description: pytest trial 
"        Create: 2018-06-30 16:25:12
"""""""""""""""""""""""""""""""""""""""""""""""


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


test_answer()
