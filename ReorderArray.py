#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReorderArray.py
# @Time    : 2018-04-02 21:05
# @Author  : zhang bo
# @Note    : 调整数组的顺序，使得奇数位于偶数的前面
"""
class Solution:
    """
    题目描述：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
            所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    """

    # 1. 快速排序的思路
    def reOrderArray1(self, array):
        """
        设置两个指针，left从左指向右，遇到偶数时停止;right从右向左，遇到奇数时停止；此时交换这两个数；直到两个指针相遇
        但是此时的奇数和奇数，偶数和偶数之间的相对位置发生了变化
        """
        if array is None or len(array) == 0:
            return None
        left = 0
        right = len(array) - 1
        while left < right:  # out-while-loop start
            while left < right and (array[left] & 0x1) != 0:  # left遇奇数时继续扫描
                left += 1
            while left < right and (array[right] & 0x1) == 0:  # right遇偶数时继续扫描
                right -= 1
            if left < right:  # 此时left遇见偶数，right遇见奇数，swap
                array[left], array[right] = array[right], array[left]
        return array

    # 2. 代码最简洁的写法：列表表达式：直接将偶数和奇数分开，再合并，O(n)的时间复杂度
    def reOrderArray2(self, array):
        x = [i for i in array if i & 0x1 == 1]
        y = [j for j in array if j & 0x1 == 0]
        return x + y

    # 3. 最常规的解法
    def reOrderArray3(self, array):
        if len(array) == 0:
            return []
        x = []
        y = []
        for i in array:
            if i & 0x1 != 0:  # 奇数
                x.append(i)
            if i & 0x1 == 0:  # 偶数
                y.append(i)
        return x + y

    # 4. 可拓展性的模板，满足多种场景，例如非负的排在负的后面。。。
    def reOrderArray4(self, array, func):
        if array is None or len(array) == 0:
            return None
        left = 0
        right = len(array) - 1
        while left < right:  # out-while-loop start
            while left < right and func(left, array):  # func返回true时继续扫描
                left += 1
            while left < right and (not func(right, array)):  # fun返回false时继续扫描
                right -= 1
            if left < right:  # 满足交换条件时，swap
                array[left], array[right] = array[right], array[left]
        return array


# 例如：奇数在偶数的前面
def oddFirst(index, array):
    return 0 if array[index] & 0x1 == 0 else 1

# 例如：负数在前正数在后
def negativeFirst(index, array):
    return 0 if array[index] > 0 else 1


if __name__ == '__main__':
    solution = Solution()
    array1 = [1, 2, 3, 4, 5]
    array2 = [1, 5, 3, 4, 2]
    array3 = [2, 4, 1, 3, 5]
    array4 = [1]
    array5 = []
    array6 = [-2, 4, 1, -3, 5]
    print(solution.reOrderArray1(array1))
    print(solution.reOrderArray2(array1))
    print(solution.reOrderArray3(array1))
    print(solution.reOrderArray4(array1, oddFirst))
    print(solution.reOrderArray4(array6, negativeFirst))
    
