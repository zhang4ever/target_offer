#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : Sort.py
# @Time    : 2018-03-26 09:45
# @Author  : zhang bo
# @Note    : 常见的各种排序算法实现
"""

class Sort:

    ## 1. 冒泡排序
    def bubbleSort(self, l):
        """
        思路：使用双重循环，依次比较两个相邻的元素，并进行交换，使得大的元素越来越右（越小的越左）。时间复杂度O(n^2)
        """
        if l is None:
            return None
        for i in range(len(l)):
            print('第%s趟' % (i + 1))
            for j in range(len(l) - (i + 1)):
                if l[j] > l[j + 1]:
                    tmp = l[j]
                    l[j] = l[j + 1]
                    l[j + 1] = tmp
                print(l)


    ## 2. 快速排序
    def quickSort(self, l, left, right):
        """
        思路：先寻找一个基准数，要寻找一个位置，将这个基准数移动至该位置，要使得比该基准数小的所有数位于该基准的左侧，
              比该基准数大的所有数位于基准的右侧.是啊金复杂度O(nlog n)
        :param left: 选中的基准位置
        :param right: 列表的最后位置
        """
        if len(l) == 0:
            return
        if left < right:
            base = l[left]  # 基准
            i = left
            j = right
            # 1. 首先确定基准的位置
            while i != j:  # 当指针i和j不相遇的时候
                while l[j] >= base and i < j:
                    j -= 1  # 首先从右向左遍历，寻找第一个比base小的数
                while l[i] <= base and i < j:
                    i += 1  # 当j指针停止遍历时，i指针开始从左向右遍历，寻找第一个比base大的数
                # i和j 都停止遍历的时候，交换
                if i < j:
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp

            l[left] = l[i]  # i=j时，找到基准该呆的位置
            l[i] = base
            print(l)
            # 2.基准将原始列表划分两部分，分别对两部分进行递归
            self.quickSort(l, left, i - 1)
            self.quickSort(l, i + 1, right)


if __name__ == '__main__':
    l = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    left = 0
    right = len(l) - 1
    sort = Sort()
    print(l)
    # sort.quickSort(l, left, right)
    sort.bubbleSort(l)
