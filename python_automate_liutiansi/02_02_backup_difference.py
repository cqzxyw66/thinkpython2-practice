#! /usr/bin/env python3 
#! -*- coding: utf-8 -*-

import os, sys
import filecmp
import re
import shutil

holderlist = []

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
        print('Usage: ' + sys.argv[0] + ' datadir targetdir')
        sys.exit()

    compareme(dir1, dir2)

    source_files = holderlist
    dir1 = os.path.abspath(dir1)

    destination_files = []
    createdir_bool = False

    for item in source_files:
        destination_dir = item.replace(dir1, dir2)

        destination_files.append(destination_dir)
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool = True
    
    if createdir_bool:
        destination_files = []
        # source_files = []
        # source_files = compareme(dir1, dir2)
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)

    print('update item:')
    for i in source_files:
        print(i)
    copy_pair = zip(source_files, destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])

if __name__ == '__main__':
    main()