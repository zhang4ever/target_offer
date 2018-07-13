#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : Accumulate.py
# @Time    : 2018-07-13 15:01
# @Author  : zhang bo
# @Note    : 求1+2+3+...+n

"""
'''
题目描述：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
思路1：使用构造函数来代替循环来求解。
思路2：使用虚函数来求解。
'''
class Solution:
    # 解法1：使用两个函数来分别表示递归以及终止条件
    def Sum_Solution(self, n):
        return self.funcN(n)

    def Sum_Solution2(self, n):
        return 0 and self.Sum_Solution(n-1) + n

    # 用该函数来代替终止条件
    def func0(self, n):
        return 0

    # 代替递归函数
    def funcN(self, n):
        func = {0: self.func0, 1: self.funcN}
        return n + func[not not n](n-1)  # f(n)=n+f(n-1)


if __name__ == '__main__':
    solution = Solution()
    n = 0
    print(solution.Sum_Solution(n))
    print(solution.Sum_Solution2(n))