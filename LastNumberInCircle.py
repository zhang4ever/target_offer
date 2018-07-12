#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : LastNumberInCircle.py
# @Time    : 2018-07-12 21:56
# @Author  : zhang bo
# @Note    : 圆圈中最后剩下的数字
"""
'''
题目描述：0,1,2...,n-1这n个数字排成一个圆圈, 从数字0开始每次从这个圆圈里删除第m个数字。求出这个圆圈里面剩下的最后一个数字。
思路1：经典的解法--环状链表。时间复杂度O(mn)
思路2：数学分析，得到地推公式f(n, m)=[f(n-1, m)+m]%n；时间复杂度o(n),空间复杂度O(1).
'''

class Solution:
    # 使用递推公式---循环
    def LastRemaining(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last

    # 使用递推公式---递归
    def LastRemaining2(self, n, m):
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        return (self.LastRemaining2(n - 1, m) + m) % n


if __name__ == '__main__':
    solution = Solution()
    n, m = 8, 3
    print(solution.LastRemaining(n, m))
    print(solution.LastRemaining2(n, m))
