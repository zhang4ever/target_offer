#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : Power.py
# @Time    : 2018-03-29 21:34
# @Author  : zhang bo
# @Note    : Power函数的使用
"""
import time

class Solution:
    """
    题目说明：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
    思路：需要考虑底数是0，指数为0或者负数的情况。
    """
    # 原始函数pow()
    def Power(self, base, exponent):
        # 直接使用pow函数
        return pow(base, exponent)

    # 手动实现
    def Power1(self, base, exponent):
        if exponent != int(exponent):
            print('错误的输入！')
            return None
        if equal(base, 0.0):
            return 0.0
        if exponent == 0:
            return 1.0
        elif exponent < 0:
            exponent = abs(exponent)
            return 1.0 / compute_pow(base, exponent)
        else:
            return compute_pow(base, exponent)

    # O(logn)的解法并且没有使用位操作
    # 指数为偶数 a^n=a^(n/2)*a^(n/2);指数为奇数时，a^n=a^((n-1)/2)*a^((n-1)/2)*a
    def Power2(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:  # 指数为正
            return base
        if exponent == -1:  # 指数为负
            return 1.0 / base
        res = self.Power2(base, int(exponent/2)) if exponent % 2 == 0 else self.Power2(base, int((exponent-1) / 2))
        res *= res
        if exponent % 2 == 1:  # 奇数
            res *= base
        return res

    # 优化：O(logn)的解法同时使用位操作,效果最好
    def Power3(self, base, exponent):

        if exponent == 0:
            return 1
        if exponent == 1:  # 指数为正
            return base
        if exponent == -1:  # 考虑指数为负
            return 1.0 / base
        res = self.Power3(base, exponent >> 1)
        res *= res
        if exponent & 0x1 == 1:  # 奇数
            res *= base
        return res


# 连乘计算pow
def compute_pow(base, exponent):
    res = 1.0
    for i in range(exponent):
        res *= base
    return res

# 比较两个小数是否相等，在考虑计算机的精度的时候
def equal(a, b):
    if (a - b) > -0.0000001 and (a + b) < 0.0000001:
        return True
    else:
        return False

# 计算运行时间
def run_time(func, m, n):
    s1 = time.clock()
    res1 = func(m, n)
    e1 = time.clock()
    print('func: %s, result:%s, time: %s' % (func.__name__, res1, (e1 - s1)))


if __name__ == '__main__':
    solution = Solution()
    base = 2
    exponent = -20
    run_time(solution.Power, base, exponent)
    run_time(solution.Power1, base, exponent)
    run_time(solution.Power2, base, exponent)
    run_time(solution.Power3, base, exponent)
    
