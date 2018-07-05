#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NumnberOf1.py
# @Time    : 2018-07-04 22:45
# @Author  : zhang bo
# @Note    : 从1中到n整数中1出现的次数
"""

'''
题目描述:输入一个整数n, 求从 1到n这n个数的十进制表示中1出现的次数。
示例：输入12, 从1到12这些整数中包含1的数字有1， 10， 11和12,1一共出现了5次
思路1: 直接使用取余的方法判断每个数字的每一位是不是有1， 然后统计，但是取余的操作的时间复杂度是O（nlogn）。所以总的时间复杂度是O(nlogn)
思路2：丛数字规律入手。
'''
class Solution:
    # 取余，统计，是按复杂度O(nlogn)
    def NumberOf1Between1AndN_Solution(self, n):
        ans = 0
        for i in range(1, n+1):
            ans += self.NumberOf1(i)
        return ans

    # 每个数字中1的个数
    def NumberOf1(self, num):
        times = 0
        while num != 0:
            if num % 10 == 1:
                times += 1
            num //= 10
        return times


if __name__ == '__main__':
    solution = Solution()
    n = 12
    print(solution.NumberOf1Between1AndN_Solution(n))
