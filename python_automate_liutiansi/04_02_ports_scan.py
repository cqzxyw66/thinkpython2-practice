#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import sys
import nmap

scan_now = [] #定义扫描主机带端口
input_data = input('请输入你要扫描的端口和主机：')
scan_now = input_data.split(' ')

if len(scan_now) != 2:
    print('输入错误，范例：\"192.168.1.0/24 80,443,22\"')
    sys.exit()
hosts = scan_now[0]
ports = scan_now[1]

try:
    nm = nmap.PortScanner() #创建端口扫描实例
except nmap.PortScannerError:
    print('Nmap模块没有找到：', sys.exc_info([0]))
    sys.exit()
except Exception as e:
    print('不可预知错误：'+ str(e))
    sys.exit()

try:
    #调用方法，参数指定扫描主机hosts，nmap扫描命令行参数 arguments
    nm.scan(hosts=hosts,
            arguments=' -v -sS -p' + ports)
except Exception as e:
    print('执行错误：' + str(e))

for host in nm.all_hosts():
    if nm[host].state() == 'up':
        print('-----------------------------------')
        print('Host: %s (%s)' % (host, nm[host].hostname()))
        print('State: %s' % nm[host].state())

        for proto in nm[host].all_protocols():
            print('-------------')
            print('协议是：%s' % proto)

            lport = list(nm[host][proto].keys())
            lport.sort()
            for port in lport:
                print('端口：%s \t状态：%s' % (port, nm[host][proto][port]['state']))
