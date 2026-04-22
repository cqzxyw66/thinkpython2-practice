#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print('Error:'+str(e))
    print('Usage: simple3.py filename1 filename2')
    sys.exit()

def readfile(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().splitlines()
            return content
        # fileHandle = open(filename, 'r')
        # text = fileHandle.read().splitlines()
        # fileHandle.close()
        # return text 
    except IOError as error:
        print('Read file Error: '+str(error))
        sys.exit()

if textfile1 == '' or textfile2 == '':
    print('Usage: simple3.py filename1 filename2')
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()

with open('diff.html', 'w', encoding='utf-8') as file:
    file.write(d.make_file(text1_lines, text2_lines))

# file = open('diff.html', 'w')
# file.write(d.make_file(text1_lines, text2_lines))
# file.close()

# print(d.make_file(text1_lines, text2_lines))