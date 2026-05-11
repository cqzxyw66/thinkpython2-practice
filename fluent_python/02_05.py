#! /usr/bin/python3
#! -*- coding: utf-8 -*-

symbol = '$￥€'

for i in tuple(ord(symbol) for symbol in symbol):
    print(i)
