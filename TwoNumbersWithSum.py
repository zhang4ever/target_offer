#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : TwoNumbersWithSum.py
# @Time    : 2018-07-09 15:45
# @Author  : zhang bo
# @Note    : 和为s的两个数字
"""
'''
题目：输入一个递增排序的数组和一个数字，在数组中查找；两个数，使得他们你的和正好是s. 如果有多对数字的和为s,输出任意一对即可。
示例：输入：{1，2，4，7，11，15}和数字15， 输出4和11
思路1:先固定一个，再找另一个O(n^2).
思路2:先设置两个指针left ,right(起始0,len-1)。如果两个和大于s,则往前找，right-1;否则往右找，left+1。时间复杂度O(n).
'''
class Solution:
    # 两个指针相向而行。时间复杂度O(n), 空间O(1)
    def FindNumbersWithSum(self, array, tsum):
        if not array or len(array) == 0:
            return []
        left = 0
        right = len(array) - 1
        while left < right:
            if array[left] + array[right] == tsum:
                return [array[left], array[right]]
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                left += 1
        return []


if __name__ == '__main__':
    solution = Solution()
    array = [1, 2, 4, 7, 11, 19]
    tsum = 10
    print(solution.FindNumbersWithSum(array, tsum))
