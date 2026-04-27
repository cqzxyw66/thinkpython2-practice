#! /usr/bin/env pyhon3
#! -*- coding: utf-8 -*-

import sys
import tkinter as tk
from tkinter import filedialog
import convert 

class TextRedirector:
    def __init__(self, text:tk.Text):
        self.text = text

    def write(self, s):
        #tk.END所有tkinter对象都支持，用来定位到最后的位置，是一个类属性。插入到文本框末尾
        self.text.insert(tk.END, s)
        #自动滚动
        self.text.see(tk.END)
        #刷新
        self.text.update()

    def flush(self):
        pass

window = tk.Tk()
window.title('CR2格式转换为JPG工具')

#获取屏幕的宽高度
screenwidth = window.winfo_screenmmwidth()
screenheight = window.winfo_screenheight()

#定义框体宽和高
width = 600
height = 400

#定义窗口初始化位置 宽度x高度+x偏移+y偏移
window.geometry('%dx%d+%d+%d' % (width, height, screenwidth/100*50, screenheight/100*20))
# window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(4, weight=1)

""" StringVar是一种特殊的变量类型，用于存储字符串值，它可以与用户界面中的组件关联，以便在用户界面中显示和更新变量的值。

StringVar的常用方法：

get()：获取StringVar对象的值。
set(value)：设置StringVar对象的值为value。
trace(callback)：为StringVar对象添加回调函数，当StringVar对象的值发生变化时，回调函数将被调用。 """
var_in = tk.StringVar()
var_out = tk.StringVar()

#选择目录按钮command
def choose_dir_in():
    dir_path = filedialog.askdirectory(title='选择目录')
    var_in.set(dir_path)

def choose_dir_out():
    dir_path = filedialog.askdirectory(title='选择目录')
    var_out.set(dir_path)

def start_convert():
    print('-'*100)
    print(f'源目录：{var_in.get()}')
    print(f'目标目录：{var_out.get()}')
    convert.convert_cr2_to_jpg(var_in.get(),var_out.get())
    print('-'*100)

#设置页面标签，标明作者信息
l = tk.Label(window, text = '作者：杨悦潼yangyuetong@yangyuetong.com', font=('Arial', 9 ), fg='black')
l.grid(row=4, columnspan=3, column=0, sticky='se')

source_directory_banner = tk.Label(window, text='源路径：',font=('Arial', 10))
source_directory_banner.grid(row=0, column=0, sticky='w')
source_directory_entry = tk.Entry(window, textvariable=var_in, font=('Arial', 10), width=55)
source_directory_entry.grid(row=0,column=1,sticky='w')
choose_directory_button = tk.Button(window, text='选择目录', command=choose_dir_in).grid(row=0, column=2)

destination_directory_banner = tk.Label(window, text='目标路径：',font=('Arial', 10))
destination_directory_banner.grid(row=1, column=0, sticky='w')
destination_directory_entry = tk.Entry(window,textvariable=var_out, font=('Arial', 10), width=55)
destination_directory_entry.grid(row=1, column=1, sticky='w')
choose_directory_button = tk.Button(window, text='选择目录', command=choose_dir_out).grid(row=1, column=2)

conver_button = tk.Button(window, text='转换', font=('Arial', 14, 'bold'), width=8,command=start_convert)
conver_button.grid(row=2, column=2, pady=5)

output_text = tk.Text(window, height=10, font=('Arial', 10))
output_text.grid(row=3,column=0, columnspan=3, sticky='w')

sys.stdout = TextRedirector(output_text)

window.mainloop()