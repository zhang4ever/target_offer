#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MaxShiftWindow.py
# @Time    : 2018-08-09 21:39
# @Author  : zhang bo
# @Note    : 滑动窗口里的最大值
"""

"""
题目描述：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
示例：如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}
"""

class Solution:
    def MaxShiftWindow(self, num, size):
        if not num or size <= 0:
            return []
        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i:size + i]))
        return res


if __name__ == '__main__':
    solution = Solution()
    num = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 4
    print(solution.MaxShiftWindow(num, size))

