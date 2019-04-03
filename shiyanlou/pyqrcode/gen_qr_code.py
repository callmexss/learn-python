#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: gen_qr_code.py
"
"        Author: xss - callmexss@126.com
"   Description: Generate QR code
"        Create: 2018-07-02 15:52:26
"""""""""""""""""""""""""""""""""""""""""""""""
import sys


try:
    from MyQR import myqr
except ImportError:
    print("Moudle install failed!")
    sys.path.append("qrcode/")
    from MyQR import myqr
    exit()


myqr.run("https://www.shiyanlou.com", save_name='plain.png')

myqr.run(
        words="https://www.shiyanlou.com",
        picture="Sources/龇牙.png",
        save_name="artistic.png"
        )

myqr.run(
        words="https://www.shiyanlou.com",
        picture="Sources/龇牙.png",
        colorized=True,
        save_name="artistic_withcolor.png"
        )

myqr.run(
        words="https://www.shiyanlou.com",
        picture="Sources/gakki.gif",
        colorized=True,
        save_name="Animated.gif"
        )
