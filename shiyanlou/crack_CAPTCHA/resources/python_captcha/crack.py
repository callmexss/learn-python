#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: crack.py
"
"        Author: xss - callmexss@126.com
"   Description: Crack captcha
"        Create: 2018-07-02 23:18:09
"""""""""""""""""""""""""""""""""""""""""""""""
import hashlib
import time
import math
import os

from PIL import Image
from pprint import pprint


class VectorCompare():

    # 计算矢量大小，计算平方和
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量间的 cos 值
    def relation(self, concordance1, concordance2):
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                # 计算相乘的和
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) *
                           self.magnitude(concordance2))


im = Image.open("captcha.gif")

# 将图片转换为8位像素模式
im.convert("P")

# 打印颜色直方图
print(im.histogram())

his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for k, v in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(k, v)

im2 = Image.new("P", im.size, 255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:
            im2.putpixel((y, x), 0)

# im2.save("output.gif")

inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if not foundletter and inletter:
        foundletter = True
        start = y

    if foundletter and not inletter:
        foundletter = False
        end = y
        letters.append((start, end))

    inletter = False

pprint(letters)

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    m.update("{0}{1}".format(str(time.time()), str(count)).encode('ascii'))
    im3.save("./{}.gif".format(m.hexdigest()))


# 把要比较的图片转为二值图，并返回成一个字典
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


v = VectorCompare()

iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

imageset = []
for letter in iconset:
    for img in os.listdir('./iconset/{}/'.format(letter)):
        temp = []
        if not img.endswith('db') and not img.endswith('.DS_Store'):
            print(img)
            temp.append(buildvector(
                Image.open('./iconset/{0}/{1}'.format(letter, img))))
        imageset.append({letter: temp})

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))

    guess = []

    for image in imageset:
        for x, y in image.items():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvector(im3)), x))

    guess.sort(reverse=True)
    print("", guess[0])
    count += 1
