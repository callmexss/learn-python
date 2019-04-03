#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: merge_two_dictionaries.py
"
"        Author: xss - callmexss@126.com
"   Description: Merge two dicts
"        Create: 2018-08-13 11:10:31
"""""""""""""""""""""""""""""""""""""""""""""""

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
print(z)
