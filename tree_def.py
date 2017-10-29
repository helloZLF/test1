#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF

import os

cur_path = os.getcwd()  # 当前绝对路径
print(os.path.basename(cur_path))
deep_len = len(cur_path.split('/'))
def func(cur_path):
    '''
    README:
    python3的解释器环境

    1, 递归循环遍历输出当前路径下的文件
    
    2,可优化方向 函数递归实现linux下tree命令的效果
    3,文件夹|++表示普通文件|--表示

    '''
    dir_list = os.listdir(cur_path)  # 列出当前路径下所有文件,形成列表
    for filename in dir_list:  # 循环列表里的每个文件
        filename_path = cur_path + '/' + filename  # 生成绝对路径
        deep_len1=len(filename_path.split('/'))
        # print(filename_path)
        if os.path.isdir(filename_path):  # 判断该文件是普通文件还是目录,如果是目录
            print('|   ' * (deep_len1-deep_len-1) + '|++' + filename)  # 格式化打印目录
            os.chdir(filename_path)  # 进入目录
            func(filename_path)
            os.chdir(os.path.dirname(filename_path))
        else:
            print('|   ' * (deep_len1-deep_len-1) + '|--' + os.path.basename(filename_path))

func(cur_path)
