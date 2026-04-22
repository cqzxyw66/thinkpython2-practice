#! /usr/bin/env python3 
#! -*- coding: utf-8 -*-

import os, sys
import filecmp
import re
import shutil

holderlist = []

def create_same_dirs(dir1: str, dir2:str):
    for root, dirs, files in os.walk(dir1):
        path = root.replace(dir1, dir2)
        if not os.path.exists(path):
            os.makedirs(path)

def compareme(dir1: str, dir2: str) -> list:
    dircomp = filecmp.dircmp(dir1, dir2) #将源目录与目标目录进行对比，生成dircmp对象
    only_in_one = dircomp.left_only #因为dir1为源目录，所以只存在dir1的则为未备份对象
    diff_in_one = dircomp.diff_files #diff_files为有变动的文件
    dirpath = os.path.abspath(dir1)

    #将更新文件名或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]

    if len(dircomp.common_dirs) > 0: #判断是否存在相同子目录，进而递归
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.abspath(os.path.join(dir2, item))))
        return holderlist
    
def main():
    if len(sys.argv) > 2: #要求输入源目录和目标备份目录
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print('Usage: ' + sys.argv[0] + ' 原目录 目标备份目录')
        sys.exit()

    create_same_dirs(dir1, dir2)
    compareme(dir1, dir2)

    source_files = holderlist
    dir1 = os.path.abspath(dir1)

    destination_files = []
    createdir_bool = False

    for item in source_files:
        destination_dir_replace = item.replace(dir1, dir2)
        destination_files.append(destination_dir_replace)

    # for item in destination_files:
    #     path = os.path.dirname(item)
    #     if not os.path.exists(path):
    #         os.makedirs(path)
        # if os.path.isdir(item):
        #     if not os.path.exists(os.path.abspath(destination_dir_replace)):
        #         os.makedirs(os.path.abspath(destination_dir_replace))
        #         # createdir_bool = True
    
    # if createdir_bool:
    #     # destination_files = []
    #     # source_files = []
    #     # source_files = compareme(dir1, dir2)
    #     for item in source_files:
    #         # destination_dir = re.sub(dir1, dir2, item)
    #         destination_dir = item.replace(dir1, dir2)
    #         destination_files.append(destination_dir)

    # print('update item:')
    # for i in source_files:
    #     print(i)
    copy_pair = zip(source_files, destination_files)
    print('---正在更新---', end='\n\n')
    for item in copy_pair:
        if os.path.isfile(item[0]):
            print('糟糕！这个文件%s 没有备份或者已经更新，Fuuuuck！我将为你备份到%s' % (item[0], item[1]))
            shutil.copyfile(item[0], item[1])

if __name__ == '__main__':
    main()