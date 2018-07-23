#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:hanzhengrong
# datetime:2018-07-13 15:45
# software: PyCharm


'''
选择排序
基本思想：
每一趟（例如第i趟）在后面n-i+1(i=1,2,3,...,n-1)个待排序元素中选取关键字最小的元素，作为
有序子序列的第i个元素，直到第n-1趟做完，待排序元素只剩下1个，就不用在选了。
时间复杂度O(n^2)

'''

def select_sort(arr):
    arr_len=len(arr)
    for i in range(arr_len-1):
        min_arr = arr[i]
        for j in range(i+1,arr_len):
            if arr[j]<arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
    return arr

elements=[5,4,6,7,9,1,2,3,8]
print(select_sort(elements))