#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF

import sys,time
"""
模拟Linux下进度条的显示进度
for i in range(0,10):#屏幕上输出进度条间隔1秒
    time.sleep(1)
    sys.stdout.write("\r"+"*"*i)#\r清空前面数据
    sys.stdout.flush()
"""

def  rate(get_size,totle_size):#定义上传或者下载文件的大小,和文件总大小
    my_perc = int(get_size / totle_size*100)#转换为百分数的数字部分
    my_stdout_left = ">"*my_perc#百分数个>字符
    my_stdout_right = '[ '+'%d'%my_perc+'%'+' ]'#进度条右边显示格式
    left_char=my_stdout_left.ljust(100,' ')#进度条总长度100个字符右边填充空字符
    sys.stdout.write("\r"+left_char+my_stdout_right )#标准输出\r清空上一次的输出内容

if __name__ == '__main__':#定义主函数
    for i in range(0,101):#for循环模拟进度
        time.sleep(0.1)#延时0.1秒
        rate(i,100)#执行rate函数







