#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : FindInPatiallySortedMatrix.py
# @Time    : 2018-03-22 22:08
# @Author  : zhang bo
# @Note    : 
"""

'''
描述：在一个二维数组中，每一行都是按照从左至右递增的顺序排序。每一列都是按照从上至下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断该数组中是否有该正数
'''
'''
解题思路：先从最右上角的数字[0][len(array[0])-1]开始查找,如果等于target，则返回T,退出程序；
         如果>target，则跳过该列；如果<target，则跳过该行；
'''

class Solution:
    # array 二维列表
    def Find(self,array, target):

        if array == []:
            return False
        rows = len(array)
        cols = len(array[0])

        i = 0
        j = cols - 1   # 最右上角
        while i < rows and j >= 0:
            if array[i][j] < target:  # 小于要找的，去掉该行
                i += 1
            elif array[i][j] > target:  # 大于要找的， 去掉该列
                j -= 1
            else:  # 小于要找的，去掉该行
                return True
        return False


if __name__ == '__main__':
    target = 20
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    array1 = []
    s = Solution()
    print(s.Find(array1, target))
