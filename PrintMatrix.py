#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PrintMatrix.py
# @Time    : 2018-04-07 22:50
# @Author  : zhang bo
# @Note    : 顺时针打印矩阵
"""

class Solution:
    """
    要求：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵：
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
    思路：m*n的矩阵，每一圈的开始位置比较特殊，坐标是（i,i）。下一圈时，i=i+1 ，但不管怎么样，都有个规律，那就是 m<=2*i
    """
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0])
        if not matrix or rows <= 0 or cols <= 0:
            return
        res = []  # 存出结果
        start = 0
        while cols > start*2 and rows > start*2:
            printMatrixInCircle(matrix, start, res)
            start += 1
        return res


def printMatrixInCircle(matrix, start, res):
    # 先打印从左到右的一行
    rows = len(matrix)
    cols = len(matrix[0])
    end_X = cols - 1 - start  # 行遍历的次数
    end_Y = rows - 1 - start  # 列遍历的次数

    for i in range(start, end_X+1):
        res.append(matrix[start][i])
        # print(matrix[start][i])
    # 打印从上到下的一列
    if start < end_Y:
        for i in range(start+1, end_Y+1):
            res.append(matrix[i][end_X])
            # print(matrix[i][end_X])
    # 打印从右到左的一行
    if start < end_X and start < end_Y:
        for i in range(end_X-1, start-1, -1):
            res.append(matrix[end_Y][i])
            # print(matrix[end_Y][i])
    # 打印从下到上的一列
    if start < end_X and start < end_Y-1:
        for i in range(end_Y-1, start, -1):
            res.append(matrix[i][start])
            # print(matrix[i][start])


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    matrix1 = [[]]
    matrix2 = [[1, 2, 3, 4]]
    matrix3 = [[1], [2], [3], [4]]
    print(matrix)
    print(solution.printMatrix(matrix))
    print(solution.printMatrix(matrix1))
    print(solution.printMatrix(matrix2))
    print(solution.printMatrix(matrix3))

