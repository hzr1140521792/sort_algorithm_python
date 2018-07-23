#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:hanzhengrong
# datetime:2018-07-13 15:46
# software: PyCharm

'''
快速排序

算法基本思想是基于分治：

在待排序列表L[1...n]中任取一个元素pivot作为基准，通过一趟排序将待排序表划分为独立的两部分
L[1...k-1]和L[k+1...n],使得L[1...k-1]中所有元素小于等于pivot，L[k+1...n]中所有元素大于等于pivot
则pivot放在了其最终位置L(k)上，这个过程称为一趟快速排序。而后分别递归地对两个子表重复上述过程，直至
每部分内只有一个元素或空为止，即所有元素放在了其最终位置上

'''
def Partition(arr,low,high):
    pivot=arr[low]  #将当前表中第一个元素设为枢轴值，对表进行划分
    while low<high:
        while low<high and arr[high]>=pivot:
            high=high-1
        arr[low]=arr[high]  #将比枢轴小的元素移动到左端

        while low<high and arr[low]<pivot:
            low=low+1
        arr[high]=arr[low] #将比枢轴大的元素移动到右端
    arr[low]=pivot #枢轴元素放到最终位置
    return low  #返回存放枢轴的最终位置

def quick_sort(arr,low,high):
    if low<high:
        pivotpos=Partition(arr,low,high) #划分
        quick_sort(arr,low,pivotpos-1)   #依次对两个子表进行递归排序
        quick_sort(arr,pivotpos+1,high)
    return arr

elements=[4,5,7,9,4,6,3,1]

print(quick_sort(elements,0,len(elements)-1))