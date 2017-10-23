#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF

def test():
    while True:
        print("请输入四位数字,退出输入break")
        in_msg=input('-->')
        if in_msg=='break':
            break

        elif  len(in_msg)==4  or len(in_msg)==5:
            try:
                int(in_msg)
                with open('data.txt','a+') as f:
                    f.write(in_msg[0]+'架'+in_msg[1]+'/'+in_msg[2]+'/'+in_msg[3:]+'\n')
                    f.flush()
            except ValueError as e:
                print("格式必须为四位数字!")
        else:
            print('重新输入!')
            continue
        

if __name__ =='__main__':
    test()
