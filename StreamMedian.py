#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : StreamMedian.py
# @Time    : 2018-07-16 15:37
# @Author  : zhang bo
# @Note    : 数据流中的中位数
"""
'''
题目描述：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
        如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值
思路1：使用排序的数组来实现。插入O(N), 获取中位数O(1)
思路2：使用堆来实现。插入O(N), 获取中位数O(1)
'''

# 1. 使用排序的数组来实现
class Solution:
    def __init__(self):
        self.res = []

    def Insert(self, num):
        self.res.append(num)
        self.res.sort()

    def GetMedian(self):
        if len(self.res) % 2 == 1:  # 奇数
            ans = self.res[len(self.res) // 2]
        else:
            ans = (self.res[len(self.res) // 2 - 1] + self.res[len(self.res) // 2]) / 2.0
        return ans

# 2. 使用最大堆和最小堆来实现
class Solution2:
    def __init__(self):
        self.min = []  # 最小堆
        self.max = []  # 最大堆

    def Insert(self, num):
        if (len(self.max) + len(self.min)) & 1 == 0:  # 总数是偶数时，添加到最大堆
            if len(self.max) > 0 and num < self.max[0]:  # 要插入的数字小于最大堆得最大值
                self.max.append(num)  # 插入最大堆
                self.MaxHeap(self.max)  # 调整最大堆
                num = self.max[0]  # 将其移出最大堆，并插入最小堆
                self.max.remove(num)
                self.MaxHeap(self.max)
            self.min.append(num)
            self.MinHeap(self.min)  # 调整最小堆
        else:
            if len(self.min) > 0 and self.min[0] < num:  # 总数是奇数时，添加到最小堆
                self.min.append(num)  # 插入最小堆
                self.MinHeap(self.min)  # 调整最小堆
                num = self.min[0]
                self.min.remove(num)  # 将其移出最小堆，并插入最大堆
                self.MinHeap(self.min)
            self.max.append(num)
            self.MaxHeap(self.max)  # 调整最大堆

    def GetMedian(self):
        if len(self.max) + len(self.min) == 0:
            return
        if (len(self.max) + len(self.min)) & 1 == 1:  # 奇数
            ans = self.min[0]
        else:  # 偶数
            ans = (self.min[0] + self.max[0]) / 2.0
        return ans

    # 调最大堆
    def MaxHeap(self, alist):
        if not alist or len(alist) == 0:
            return
        if len(alist) == 1:
            return alist
        for i in range(len(alist) // 2 - 1, -1, -1):
            k = i  # 当前
            temp = alist[i]  # 当前值
            heap = False  # 是否是堆
            while not heap and 2 * k < len(alist) - 1:  # 不是最大堆，需调整
                index = 2 * i + 1  # 当前节点的左孩子, 记录较大的孩子
                if index < len(alist) - 1:
                    if alist[index] < alist[index + 1]:  # 右孩子大
                        index += 1
                if temp > alist[index]:  # 父节点均大于其子节点，当前满足最大堆
                    heap = True
                else:  # 父节点小，需要交换
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    # 调整最小堆
    def MinHeap(self, alist):
        if not alist or len(alist) == 0:
            return
        if len(alist) == 1:
            return alist
        for i in range(len(alist) // 2 - 1, -1, -1):
            k = i  # 当前
            temp = alist[i]  # 当前值
            heap = False  # 是否是堆
            while not heap and 2 * k < len(alist) - 1:  # 不是最小堆，需调整
                index = 2 * i + 1  # 当前节点的左孩子
                if index < len(alist) - 1:
                    if alist[index] > alist[index + 1]:  # 左孩子大
                        index += 1
                if temp <= alist[index]:  # 父节点小于其子节点，当前满足最小堆
                    heap = True
                else:  # 父节点大，需要交换
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp


if __name__ == '__main__':
    solution = Solution2()
    solution.Insert(1)
    solution.Insert(9)
    solution.Insert(3)
    solution.Insert(5)
    solution.Insert(8)
    solution.Insert(6)

    print(solution.GetMedian())
