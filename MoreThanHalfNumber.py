#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MoreThanHalfNumber.py
# @Time    : 2018-07-03 15:17
# @Author  : zhang bo
# @Note    : 数组中出现次数超过一半的数字
"""
class Solution:
    """
    题目描述：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    实例：例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
    思路1：对于一个出现的个数超过长度一般的数，如果一个数组中存在这样的数，那一定是位于数组的中位数的位置。所以先对数组进行排序，
        为了使排序的时间最少，使用快速排序，基于快速排序的思路，时间复杂度O(n)。然后寻找中位数，并验证中位数所在的数字出现的次数。
    思路2：如果一个数字出席拿的次数超过数组的长度的一半，那就说明该数字出现的次数哟啊波其他的所有出现的次数的和还要多。所以遍历数组，如果
        下一个数组与之前保存的不一样，次数-1， 如果一样，次数+1， 如果次数=0，则保存下一个数字，次数设1，最后一个次数=1的就是结果。
    """

    # 解法一：使用快速排序(改变数组原本顺序), O(n)
    def MoreThanHalfNum(self, numbers):

        if not self.validateNumber(numbers):
            return 0
        middle = len(numbers) >> 1
        left = 0
        right = len(numbers) - 1
        self.quickSort(numbers, left, right)  # 快速排序（也可直接使用内置函数sort）
        res = numbers[middle]  # 中位数
        if not self.isMoreThanHalf(numbers, res):
            return 0
        return numbers[middle]


    # 解法二：不使用排序（不改变数组原本的顺序）O(n)
    def MoreThanHalfNum2(self, numbers):

        if not self.validateNumber(numbers):
            return 0
        times = 1
        res = numbers[0]
        for i in range(1, len(numbers)):
            if times == 0:  # 保存下一个，times=1
                res = numbers[i]
                times = 1
            if numbers[i] != res:  # 不等，times-1
                times -= 1
            else:  # 等于，times+1
                times += 1
        if not self.isMoreThanHalf(numbers, res):  # 检验是否>1/2 length
            return 0
        return res


    # 判断数组是否合法
    def validateNumber(self, numbers):
        if len(numbers) <= 0 or numbers is None:
            return False
        return True

    # 验证是否超过数组长度一半
    def isMoreThanHalf(self, numbers, res):
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                times += 1
        if times > len(numbers) >> 1:
            return True
        return False

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

            l[left] = l[i]  # i=j时，找到基准该呆的位置
            l[i] = base
            print(l)
            # 2.基准将原始列表划分两部分，分别对两部分进行递归
            self.quickSort(l, left, i - 1)
            self.quickSort(l, i + 1, right)


if __name__ == '__main__':
    solution = Solution()
    numbers1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    numbers2 = []
    numbers3 = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    numbers4 = [1]
    print(solution.MoreThanHalfNum(numbers1))
    print(solution.MoreThanHalfNum2(numbers3))