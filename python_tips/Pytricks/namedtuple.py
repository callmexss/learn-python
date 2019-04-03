#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: namedtuple.py
"
"        Author: xss - callmexss@126.com
"   Description: Named tuple as class
"        Create: 2018-08-13 11:15:19
"""""""""""""""""""""""""""""""""""""""""""""""

from collections import namedtuple


Person = namedtuple('Person', 'name age')

Tom = Person('Tom', 20)
Lily = Person('Lily', 22)


def print_info(who):
    print('{} is {} years old.'.format(who.name, who.age))


print_info(Tom)
print_info(Lily)
