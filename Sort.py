#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : Sort.py
# @Time    : 2018-03-26 09:45
# @Author  : zhang bo
# @Note    : 常见的各种排序算法实现
"""

class Sort:

    # 1. 快速排序：平均复杂度O(nlog(n)), 最好O(nlog(n)), 最坏O(n^2)
    def QuickSort(self, l, left, right):
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
                if i < j:  # i和j 都停止遍历的时候，交换
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp

            l[left] = l[i]  # i=j时，找到基准该呆的位置
            l[i] = base
            print(l)
            # 2.基准将原始列表划分两部分，分别对两部分进行递归
            self.QuickSort(l, left, i - 1)
            self.QuickSort(l, i + 1, right)

    # 2. 归并排序, 平均、最好。最坏的时间复杂度都是O(nlog(n))
    def MergeSort(self, l):
        """
        思路：先将数组依次2等分， 然后再合并
        """
        left = 0
        right = len(l) - 1
        tmp = ['#']*len(l)  # 辅助数组, 用特殊字符来初始化
        self.sort(l, left, right, tmp)

    def sort(self, l, left, right, tmp):
        if left < right:
            mid = (left + right) // 2
            self.sort(l, left, mid, tmp)  # 划分左边
            self.sort(l, mid + 1, right, tmp)  # 划分右边
            self.merge(l, left, mid, right, tmp)  # 合并两个子数组

    def merge(self, l, left, mid, right, tmp):
        i = left
        j = mid + 1
        t = 0  # 这里的临时指针的作用就是在每次递归合并的时候，重新指向辅助数组的0位置，防止数组保留每次递归的所有值
        while i <= mid and j <= right:
            if l[i] <= l[j]:
                tmp[t] = l[i]
                t += 1
                i += 1
            else:
                tmp[t] = l[j]
                t += 1
                j += 1
        while i <= mid:  # 将左子数组剩下的直接插入
            tmp[t] = l[i]
            t += 1
            i += 1
        while j <= right:  # 将右子数组剩下的直接插入
            tmp[t] = l[j]
            t += 1
            j += 1
        # 将已经合并好的复制到原始的数组中
        t = 0
        while left <= right:
            l[left] = tmp[t]
            t += 1
            left += 1
        print(l)

    # 3. 冒泡排序:平均的复杂度O(nlog(n))，最好O(nlog(n)), 最坏O(n^2)
    def BubbleSort(self, l):
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

    # 4.插入排序：平均复杂度O(n^2), 最好O(n), 最坏O(n^2)
    def InsertSort(self, l):
        """
        思路：刚开始时以第1个元素作为已经排好序的，然后依次将后面的元素看做待插入的元素，依次移动已排序的合适的位置
        """
        n = len(l)
        print('第1趟:%s' % l)
        for i in range(1, n):
            tmp = l[i]
            j = i
            while tmp < l[j - 1] and j > 0:  # [i, 0]逆序
                l[j] = l[j - 1]  # 依次后移
                j -= 1
            l[j] = tmp  # 插入
            print('第%s趟:%s' % (i + 1, l))


if __name__ == '__main__':
    l = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    left = 0
    right = len(l) - 1
    sort = Sort()
    print(l)
    # sort.quickSort(l, left, right)
    # sort.BubbleSort(l)
    # print(sort.InsertSort(l))
    # sort.MergeSort(l)
