#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : KLeastNumbers.py
# @Time    : 2018-07-04 11:05
# @Author  : zhang bo
# @Note    : 最小的K个数
"""
'''
题目描述：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
思路1：排序，直接取前k个，但是时间复杂度O(nlogn)
思路2：使用快速排序思想，时间复杂度O(n)
思路3：创建一个容量尾k的容器，以此读入输入数据加入到容器中，如果容器满了，则比较容器中的最大值和带添加的数据，如果待添加的小，则替换掉容器中的
      最大值，否则跳过；最后容器中剩下的数即使满足条件结果。这个插入过程使用最大堆或者最小堆来实现的话，时间复杂度为O(nlogk)
'''


class Solution:
    # 采用快速排序的分区思路，但不需要进行完整的排序
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < 0 or k <= 0 or len(tinput) < k or tinput is None:
            return
        left = 0
        right = len(tinput) - 1
        index = self.Partition(tinput, left, right)  # 找到划分的位置
        while index != k-1:
            if index > k-1:  # 说明要的结果在基准的左侧
                right = k-1
                index = self.Partition(tinput, left, right)
            else:  # 说明要的结果在基准的两侧都有
                left = index + 1
                index = self.Partition(tinput, left, right)
        # 找到了最合适的划分位置，这样划分后，base前面的数就刚好是最小的k个，但是不一定是排好序的
        return tinput[:k]

    # 解法2： 最大堆， 时间复杂度O(n*logk)，且不需要修改原始的数组，所有的操作都在容器中进行。适合处理大量数据
    def GetLeastNumbers_Solution2(self, tinput, k):
        import heapq
        if len(tinput) < 0 or k <= 0 or len(tinput) < k or tinput is None:
            return []
        if len(tinput) == k:
            return heapq.nlargest(k, tinput)[::-1]

        res = []  # 定义1个容器
        for data in tinput:
            if len(res) < k:  # 容器没满
                res.append(data)
            else:  # 满了，借助最大堆来处理
                res = heapq.nlargest(k, res)  # 将容器里的数据构造最大堆
                if data < res[0]:  # < max_val
                    res[0] = data
                else:  # >= max_val, jump
                    continue
        return res[::-1]

    # 解法3：直接快速排序，时间复杂度O(nlogn)
    def GetLeastNumbers_Solution3(self, tinput, k):
        if len(tinput) < 0 or k <= 0 or len(tinput) < k or tinput is None:
            return []
        left = 0
        right = len(tinput) - 1
        self.quickSort(tinput, left, right)
        return tinput[:k]

    # 快速排序
    def quickSort(self, l, left, right):
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
            # i=j时，找到基准该呆的位置,此时会将数组以base划分为两部分，比base小的在base的左边，比base大的在base的右边
            l[left] = l[i]
            l[i] = base
            # print(l)
            # 2.基准将原始列表划分两部分，分别对两部分进行递归
            self.quickSort(l, left, i - 1)
            self.quickSort(l, i + 1, right)

    # 分组思路，使用快速排序的做法,返回划分的位置
    def Partition(self, l, left, right):
        base = l[left]
        i, j = left, right
        while i != j:
            while l[j] > base and i < j:
                j -= 1
            while l[i] < base and i < j:
                i += 1
            # 各自找到需要交换的元素，就交换
            l[i], l[j] = l[j], l[i]
        # i=j,找打到了基准的值该在的位置，返回
        return i


if __name__ == "__main__":
    solution = Solution()
    tinput1 = [3, 4, 1, 7, 6, 2, 0]
    tinput2 = []
    tinput3 = [1, 2, 3]
    k = 5
    print(solution.GetLeastNumbers_Solution(tinput1, k))
    print(solution.GetLeastNumbers_Solution2(tinput1, k))
    print(solution.GetLeastNumbers_Solution3(tinput1, k))