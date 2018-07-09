#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NumbersAppearOnce.py
# @Time    : 2018-07-09 14:35
# @Author  : zhang bo
# @Note    : 数组中只出现一次的数字
"""
'''
题目描述：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度O(n),空间复杂度O(1)
示例：输入数组{2,4,3,6,3,2,5,5}。输出{4,6}
思路：先对数组中的每个数进行异或运算，根据结果的2进制形式中的第一个为1的位置(flag)将原始的数组划分为两个部分，一个是包含数组中的flag位为1
    的数，另一个就是剩下的。然后 对这两个数组进行异或运。最后的结果分别就是两个子数组中只出现一次的数字。由于只遍历了一次数组，且没有引入、
    额外的空间开销，所以时间复杂度O(n)，空间复杂度O(1)
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array or len(array) == 0:
            return
        result_OR = 0
        for i in array:  # 一次异或
            result_OR = result_OR ^ i
        flag = self.FindFirst1Bit(result_OR)  # 在异或的结果找到第一个为1的位
        res1, res2 = 0, 0
        for i in array:  # 遍历数组，划分并对划分的数组进行异或运算
            if self.Is1Bit(i, flag):
                res1 = res1 ^ i
            else:
                res2 = res2 ^ i
        return [res1, res2]

    # 在以异或的结果中找到flag位为1
    def FindFirst1Bit(self, result):
        flag = 0
        while result & 1 == 0 and flag <= 32:  # 最后一位是不是1
            flag += 1
            result = result >> 1
        return flag

    # 判断一个数字的flag位是不是1
    def Is1Bit(self, num, flag):
        num = num >> flag
        return num & 1


if __name__ == '__main__':
    solution = Solution()
    array1 = [2, 4, 3, 6, 3, 2, 5, 5]
    array2 = [1, 2, 3, 4]
    array3 = []
    print(solution.FindNumsAppearOnce(array1))
    print(solution.FindNumsAppearOnce(array2))
    print(solution.FindNumsAppearOnce(array3))
