#! /usr/bin/env python3
#! -*- coding: utf-8 *-*

import xlsxwriter
import io
import urllib.request as urllib2

workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook._add_sheet('sheet1')

image_data = io.BytesIO(urllib2.urlopen('https://www.python.org/static/img/python-logo.png').read())
worksheet.insert_image('B5', 'python-logo.png', {'image_data': image_data})

workbook.close()