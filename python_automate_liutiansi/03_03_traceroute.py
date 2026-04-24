#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import os,sys,time,subprocess
import warnings, logging
from scapy.all import traceroute,traceroute6

# os.environ['PATH'] += os.pathsep + r'D:\SoftwareInstall\Graphviz-14.1.5-win32\bin'
warnings.filterwarnings('ignore', category=DeprecationWarning)
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

domains = input('请输入你要探测的域名或IP地址：')
ip_protol = input('请输入你要选择的ip协议，4:ipv4，6：ipv6：')
if ip_protol == '4':
    ip_protol = traceroute
elif ip_protol == '6':
    ip_protol = traceroute6
target = domains.split(',')
print(os.environ['PATH'])
dport = [443]

if len(target) >= 1 and target[0] != '':
    res,unans = ip_protol(target, dport=dport, retry=-2)
    res.graph(target = '> test.svg', 
              type='svg',
              prog = r'D:\SoftwareInstall\Graphviz-14.1.5-win32\bin\dot.exe')
    time.sleep(1)
else:
    print('ip或域名输入数量错误')