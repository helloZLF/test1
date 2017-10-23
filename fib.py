#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF


a=0
b=1
n=0
list1=[]
while n<10:
    list1.append(a)
    a, b = b, a + b
    print(list1)
    n+=1
n=0
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(9))
