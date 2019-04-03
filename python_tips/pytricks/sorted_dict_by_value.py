#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: sorted_dict_by_value.py
"
"        Author: xss - callmexss@126.com
"   Description: Sorted dict by value
"        Create: 2018-08-13 10:46:25
"""""""""""""""""""""""""""""""""""""""""""""""

import random
import string
import operator


seq = list(set([random.randint(0, 25) for x in range(10)]))
chars = [string.ascii_lowercase[i] for i in seq]

dic = dict(zip(seq, chars))
print(dic)

print('sorted by lambda')
dic_as_sorted_by_lambda = sorted(dic.items(), key=lambda item: item[1])
print(dic_as_sorted_by_lambda)

print('sorted by operator')
dic_as_sorted_by_operator = sorted(dic.items(), key=operator.itemgetter(1))
print(dic_as_sorted_by_operator)
