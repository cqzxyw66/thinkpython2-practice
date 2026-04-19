#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from IPy import IP
ip_s = input('Pls input an IP or net-range: ')
ips = IP(ip_s)

if ips.len() > 1: #为一个网络地址
    print('net: %s' % ips.net()) #输出网络地址
    print('netmask: %s' % ips.netmask()) #输出网络掩码地址
    print('broadcast: %s' % ips.broadcast()) #输出网络广播地址
    print('reverse address: %s' % ips.reverseNames()[0]) #输出地址反向解析
    print('subnet: %s' % ips.len())
else:  #为单个地址
    print('reverse address: %s' % ips.reverseNames())

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())