#/usr/bin/python3
# -*- coding: utf-8 -*-
'''
File:          1_assert_in_python.py
File Created:  Wednesday, 3rd April 2019 8:13:17 pm
Author:        xss (callmexss@126.com)
Description:   assert expression in python
               
-----
Last Modified: Wednesday, 3rd April 2019 8:13:20 pm
Modified By:   xss (callmexss@126.com)
-----
'''

# ? basic stuff about assert
# - useful for debug, should consider use it properly.
# - assertions are meant to be internal self-checks for your program.
# ? syntax for the assert statement
# - assert_stmt ::= "assert" expression1 ["," expression2]
# - expression1 is the condition we test,
# - optional expression2 is an error message displayed when the assert failed.
# . if __debug__:
# .     if not expression1:
# .         raise AssertionError(expression2)
# ? important ones
# ! keep in mind it is a debug aid.
# ! inform developers about unrecoverable errors in a program.
def applay_discount(product, discount):
    """Applay discount on product.
    
    :param product: some product
    :type product: map
    :param discount: discount rate
    :type discount: float
    :return: price
    :rtype: int
    """
    price = int(product["price"] * (1.0 - discount))
    assert 0 < price < product["price"]
    return price


if __name__ == "__main__":
    shoes = {'name': 'Fancy Shoes', 'price': 14900}
    print(applay_discount(shoes, 0.25))
    print(applay_discount(shoes, 2))