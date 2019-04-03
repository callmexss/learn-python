#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: concatenate_str.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-06-30 15:41:01
"""""""""""""""""""""""""""""""""""""""""""""""
from __future__ import print_function

import time
import sys


if sys.version_info[0] > 2:  # python3
    is_py3 = True
else:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    is_py3 = False


def decorator(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


# worse
@decorator
def concatenate_str_worse():
    nums = ""
    for n in range(100000):
        nums += str(n)
    return nums


# good
@decorator
def concatenate_str_good():
    nums = []
    for n in range(100000):
        nums.append(str(n))
    return ''.join(nums)


# better
@decorator
def concatenate_str_better():
    nums = [str(n) for n in range(100000)]
    return ''.join(nums)


# best
@decorator
def concatenate_str_best():
    nums = map(str, range(100000))
    return ''.join(nums)


if "__name__" == "__main__":
    concatenate_str_worse()
    concatenate_str_good()
    concatenate_str_better()
    concatenate_str_best()

