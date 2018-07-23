#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:hanzhengrong
# datetime:2018-07-13 15:01
# software: PyCharm

#冒泡排序思想：
# 假设待排序表长度为n，从后往前（或从前往后）两两比较相邻元素的值，若为逆序（即A[i-1]>A[i]），则交换它们，直到序列比较完

#待排序元素
import random

a=[1,3,2,6,7,2,5]
b=[5,4,5,7,9,3,2,3,4]
c=[int(random.random()*10) for i in range(50)]
print(c)

def  bubleSort(list):
    for i in range(len(list)): #从前向后开始排序
        flag=False #标志是否还需要比较
        for j in range(len(list)-1,i,-1): #从后向前开始比较
            if list[j]<list[j-1]: #小的在前，大的在后
                list[j],list[j-1]=list[j-1],list[j]
                flag=True
        if flag==False:
            break
    return list

print(bubleSort(a))
print(bubleSort(b))
# print([x for x in range(3,1,-1)])
print(bubleSort(c))