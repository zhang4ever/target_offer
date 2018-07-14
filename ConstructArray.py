#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ConstructArray.py
# @Time    : 2018-07-14 10:36
# @Author  : zhang bo
# @Note    : 构建乘积数组
"""
'''
题目描述：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
        不能使用除法。
思路：最后的结果可以看作是两个新的数组的乘积。B = C*D, C[i]=C[i-1]*A[i-1], D[i]=D[i+1]*A[i+1]
'''

class Solution:
    def multiply(self, A):
        C, D = [1] * len(A), [1] * len(A)

        for i in range(1, len(A)):
            C[i] = C[i - 1] * A[i - 1]
        for i in range(len(A) - 2, -1, -1):
            D[i] = D[i + 1] * A[i + 1]
        B = [i * j for i, j in zip(C, D)]
        del C, D
        return B

    def multiply2(self, A):
        if not A or len(A) == 0:
            return
        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        tmp = 1
        for i in range(len(A) - 2, -1, -1):
            tmp = tmp * A[i + 1]
            B[i] = B[i] * tmp
        return B


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4, 5]
    print(solution.multiply(A))
    print(solution.multiply2(A))
