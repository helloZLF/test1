#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF

'''
README:

    1, 三层循环遍历输出当前路径下的文件
    2, 只适合三层
    3,可优化方向 函数递归实现linux下tree命令的效果
    4,文件夹|++表示普通文件|--表示

'''

import os

cur_path = os.getcwd()#当前绝对路径
print(os.path.basename(cur_path))#打印当前路径
dir_list=os.listdir(cur_path)#列出当前路径下所有文件,形成列表
for filename in dir_list:#循环列表里的每个文件
    filename_path = cur_path+'/'+filename#生成绝对路径
    # print(filename_path)
    if os.path.isdir(filename_path):#判断该文件是普通文件还是目录,如果是目录
        os.chdir(filename_path)#进入目录
        # print('---',os.getcwd())
        print('|   '*0+'|++'+filename)#格式化打印目录
        dir_list1=os.listdir(filename_path)
        for filename1 in dir_list1:
            filename_path1=filename_path+'/'+filename1
            if os.path.isdir(filename_path1):
                os.chdir(filename_path1)
                print('|   '*1+'|++'+filename1)
                dir_list2=os.listdir(filename_path1)
                for filename2 in dir_list2:
                    filename_path2 = filename_path1+'/'+filename2
                    if os.path.isdir(filename_path2):
                        os.chdir(filename_path2)
                        print('|   '*2+'|++'+filename2)
                        dir_list3 = os.listdir(filename_path2)
                        for filename3 in dir_list3:
                            filename_path3 = filename_path2 + '/' + filename3
                            if os.path.isdir(filename_path3):
                                os.chdir(filename_path3)
                                print('|   ' * 3 + '|++' + filename3)

                                os.chdir(os.path.dirname(filename_path3))
                            else:
                                print('|   ' * 3 + '|--' + filename3)
                        os.chdir(os.path.dirname(filename_path2))
                    else:
                        print('|   '*2+'|--'+filename2)
                os.chdir(os.path.dirname(filename_path1))
            else:
                print('|   ' * 1 + '|--' + os.path.basename(filename_path1))

        os.chdir(os.path.dirname(filename_path))
        # print('***',os.getcwd())
    else:
        print('|   '*0+'|--'+os.path.basename(filename_path))


