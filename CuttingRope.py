#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : CuttingRope.py
# @Time    : 2018-07-20 10:10
# @Author  : zhang bo
# @Note    : 剪绳子
"""

'''
题目描述：给一根长度为n的绳子，请将绳子剪成m段（m,n都是整数，且都大于1），每段绳子的查长度记为K[0],K[1]...,K[m].请问k[0]*k[1]*...*k[m]
        可能的最大乘积是多少？
示例：当绳子的长度是8时，我们将它剪成长度为别是2、3、3的三段，此时得到的嘴大乘积是18。
思路1：动态规划。f[n]=max(f[i]*f[n-i]), i=1,2,...,n.采用自下而上的策略，先求出子问题的最优解，然后依次求出其他的。
思路2：贪婪算法。当n>=5的时候，将绳子尽可能的多剪成长度=3的，如果最后剩下的不够剪成3的，则尽可能的多剪成长度=2的。
'''

class Solution:
    # 使用动态规划
    def maxProductAfterCutting_Dynamic(self, n):
        if n < 2:
            return 0  # 因为至少要切成两段
        if n == 2:
            return 1  # 2段，每段长=1
        if n == 3:
            return 2  # 可以剪成3段（每段=1）或则两段（1和2），所以max(1,2)=2

        products = [0]*(n+1)  # 存储最优的解
        # 确定子问题的最优解
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, n + 1):
            max_prod = 0
            for j in range(1, i//2+1):
                product = products[j] * products[i-j]
                if max_prod < product:
                    max_prod = product
                products[i] = max_prod
        max_prod = products[n]
        return max_prod

    # 使用贪心算法
    def maxProductAfterCutting_Greed(self, n):
        if n < 2:
            return 0  # 因为至少要切成两段
        if n == 2:
            return 1  # 2段，每段长=1
        if n == 3:
            return 2  # 可以剪成3段（每段=1）或则两段（1和2），所以max(1,2)=2
        timesOf3 = n // 3
        # 因为3*1的结果没有2*2的优
        if n - timesOf3*3 == 1:
            timesOf3 -= 1
        timesOf2 = (n-timesOf3*3)//2
        max_prod = pow(3, timesOf3)*pow(2, timesOf2)
        return max_prod


if __name__ == '__main__':
    solution = Solution()
    n = 8
    print(solution.maxProductAfterCutting_Dynamic(n))
    print(solution.maxProductAfterCutting_Greed(n))
