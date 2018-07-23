#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:hanzhengrong
# datetime:2018-07-13 15:46
# software: PyCharm

'''
二叉堆具有以下性质：
1.父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值
2.每个节点的左右子树都是二叉堆（最大堆或最小堆）


算法步骤：
1.构建初始堆：n个节点的完全二叉树，最后一个节点是第[n/2]个节点的孩子。
对第[n/2]个节点为根的子树筛选（对于大根堆：若根节点的关键字小于左右子女中关键字较大者，则交换），
使该子树为堆。之后依次向前调整，直到以所有节点为根节点的子树都为最大堆为止；

2.堆排序：堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。
思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。
第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。
由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。

3.调整堆
根据第1个步骤的方法，调整堆


伪代码：

HEAPSORT(A)
BULD-MAX-HEAP(A)
for i=A.length downto 2
    exchange A[1] with A[i]
    A.heap-size=A.heap-size-1
    MAX-HEAPIFY(A,1)

'''
#
elements=[5,4,5,7,9,3,2,3,4]





# 网上的答案

def heapSort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #两个子节点比较取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

print(heapSort(elements))