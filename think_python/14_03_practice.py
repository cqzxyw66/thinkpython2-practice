import os
import string
import subprocess
import time
from time import asctime
from os.path import join, getsize

def dedicated_file_ext(path, *ext):
    b = list()
    c = list()
    path_str = path.strip()
    for root, dirnames, files in os.walk(path_str):
        file_path = [os.path.join(root, name) for name in files]
        for i in file_path:
            file_path_ext = os.path.splitext(i)[1],
            c.append(i)
            if ext == file_path_ext:
                b.append(i)
    if ext == ():
        return c
    else:
        return b

def caculate_md5(file):
    ps_cmd = f'Get-FileHash -algorithm md5 "{file}" | format-list Hash'
    t = subprocess.run([
        'powershell.exe',
        '-command',
        ps_cmd
    ], text=True, capture_output=True, encoding='utf-8').stdout
    try: 
        t = t.strip().split()[2]
    except:
        print(f'{file} cannot hash')
    return t

def duplicate_file_dict(path, *ext):
    a = dict()
    files = dedicated_file_ext(path, *ext)
    for i in files:
        md5 = caculate_md5(i)
        mtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(i)))
        ctime = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getctime(i)))
        atime = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getatime(i)))
        filename_time = [(i, f'修改时间:{mtime} 创建时间:{ctime} 访问时间:{atime}')]
        if md5 not in a:
            a[md5] = filename_time
        else:
            a[md5] += filename_time
    b = dict()
    for j in a:
        length = len(a[j])
        if length > 1:
            b[j] = a[j]
    return b

a = duplicate_file_dict(r'D:\SGMW\python', '.pdf')
for key in a:
    print(key, a[key])
    print('---')