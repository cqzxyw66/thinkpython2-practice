#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import dns.resolver

domain, query_type = input('请输入你要查询的域名和类型，用英文逗号分开：').split(',')

try:
    A = dns.resolver.resolve(domain, query_type)
    print('所查域名的%s记录为：' % query_type)

    for i in A.response.answer:
        for j in i.items:
            print(j)
except:
    print('对不起，你输入的域名和类型不匹配或不存在')