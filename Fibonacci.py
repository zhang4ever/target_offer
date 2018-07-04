#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : Fibonacci.py
# @Time    : 2018-03-27 17:41
# @Author  : zhang bo
# @Note    : 
"""
'''
描述：写一个函数，输入n， 求斐波那契数列的第n项
思路：直接使用递归的方法简单，但是时间复杂度高；由于递归的时候，重复的计算了很多节点的值，所以避免这些值的重复计算就可以
        降低时间复杂度
拓展：关于斐波那契的应用。例如：一直青蛙跳台阶，可以跳1级，也可以跳2级，问你这只青蛙跳上n个台阶，共有多少种跳法；
拓展解法：
    显然，f(0)=0;对于1个台阶的，f(1) = 1; 对于n个台阶的，加入第一次跳1级，那么剩下的n-1个，就有f(n-1)种；加入第一次跳2级，
    那么剩下的n-2个，就有f(n-2)种。综上，对于n个台阶的，就有f(n)=f(n-1)+f(n-2)。典型的斐波那契的应用。
'''

class Solution:

    # 递归法（低效）--时间复杂度呈指数递增
    def Fibonacci1(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci1(n-1) + self.Fibonacci1(n-2)

    # 使用复杂度为O(n)的解法
    def Fibonacci2(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        res = 0
        res_pre2 = 0  # F(n-1)
        res_pre1 = 1  # F(n-2)
        for i in range(2, n + 1):
            res = res_pre1 + res_pre2
            res_pre2 = res_pre1
            res_pre1 = res
        return res


    # Fibonacci的变体1：一个青蛙，一次能跳1个或2个台阶，问跳上n个台阶共有多少种跳法
    def Fibonacci3(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = 0
        res_pre2 = 1  # F(n-1)
        res_pre1 = 2  # F(n-2)
        for i in range(n-2):
            res = res_pre1 + res_pre2
            res_pre2 = res_pre1
            res_pre1 = res
        return res


    # Fibonacci的变体2：一个青蛙，一次能跳1个或2或者...或者n个台阶，问跳上n个台阶共有多少种跳法
    def Fibonacci4(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        # else:
            # 递归的解法
            # return 2 * self.Fibonacci4(n - 1)

        res = 1
        res_pre = 1  # F(n-1)
        for i in range(n - 1):
            res = 2*res_pre
            res_pre = res
        return res

if __name__ == '__main__':
    solution = Solution()
    n = 100
    # print(solution.Fibonacci1(n))  # 奔溃
    print(solution.Fibonacci2(n))  # fast and right 
    print(solution.Fibonacci2(n))
    print(solution.Fibonacci4(n))
