#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import os,sys
import time
import sys
import pycurl

URL = 'https://www.cctv.com'
c = pycurl.Curl() #创建pycurl一个实例
c.setopt(pycurl.URL, URL) #定义请求URL常量
c.setopt(pycurl.CONNECTTIMEOUT, 5) #定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT, 5) #定期请求超时时间
c.setopt(pycurl.NOPROGRESS, 1) #屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE, 1) #完成交互后强制断开连接，不重用
c.setopt(pycurl.MAXREDIRS, 1) #指定HTTP重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30) # 设置保存DNS信息的时间为30秒

# 创建一个文件对象，以wb方式打开，用来存储返回的http头部及body内容
indexfile = open(os.path.dirname(os.path.realpath(__file__)) + '/content.text', 'wb')
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)

try:
    c.perform() #提交请求
except Exception as e:
    print('连接错误：', str(e))
    indexfile.close()
    c.close()

    sys.exit()

namelookup_time = c.getinfo(c.NAMELOOKUP_TIME) #获取DNS解析时间
connect_time = c.getinfo(c.CONNECT_TIME) #获取建立连接的时间
pretransfer_time = c.getinfo(c.PRETRANSFER_TIME) # 获取从建立连接到准备传输所消耗的时间
starttransfer_time = c.getinfo(c.STARTTRANSFER_TIME) #获取从建立连接到传输开始所消耗的时间
total_time = c.getinfo(c.TOTAL_TIME) #获取传输的总时间
http_code = c.getinfo(c.HTTP_CODE) #获取HTTP状态码
size_download = c.getinfo(c.SIZE_DOWNLOAD) #获取下载数据包大小
header_size = c.getinfo(c.HEADER_SIZE) #获取HTTP头部大小
speed_download = c.getinfo(c.SPEED_DOWNLOAD) #获取平均下载速度

#格式化输出相关数据
print('本机发起的IP为：%s' % c.getinfo(c.LOCAL_IP))
print(f'服务器IP为：{c.getinfo(c.PRIMARY_IP)}')
print('服务器端口为：%s' % c.getinfo(c.PRIMARY_PORT))
print(f'HTTP状态码：{http_code}')
print(f'DNS解析时间：{namelookup_time * 1000} ms')
print(f'建立连接时间：{connect_time * 1000} ms')
print(f'准备传输时间：{pretransfer_time * 1000} ms')
print(f'传输开始时间：{starttransfer_time * 1000} ms')
print(f'下载数据包大小：{size_download} byte/s')
print(f'HTTP头部大小：{header_size} bytes')
print(f'平均下载速度：{speed_download} byte/s')
indexfile.close()
c.close()