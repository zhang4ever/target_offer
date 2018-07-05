#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : UglyNumber.py
# @Time    : 2018-07-05 19:51
# @Author  : zhang bo
# @Note    : 丑数
"""
'''
题目描述：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 
        习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路1：根据丑数的定义依次判断每个数；时间复杂度高，但是算法容易理解
思路2：使用空间换时间。事先用数组存储已经生成的丑数，会占用一部分的内存，但时间复杂度低。
'''

class Solution:
    # 解法1：直观但并不高效的解法
    def GetUglyNumber_Solution(self, index):
        if index < 0:
            return 0
        number = 0
        times = 0  # 记录丑数的个数
        while times < index:
            number += 1
            if self.IsUgly(number):
                times += 1
        return number

    # 解法2：使用空间换时间，时间效率低
    def GetUglyNumber_Solution2(self, index):
        if index <= 0:
            return 0
        ugly_numbers = [1] * index  # 丑数
        next_num = 1
        multi2, multi3, multi5 = 0, 0, 0  # 分贝对已有的数乘2,3,5后的索引
        while next_num < index:
            curr_min = min(ugly_numbers[multi2] * 2, ugly_numbers[multi3] * 3, ugly_numbers[multi5] * 5)  # 记录最小值
            ugly_numbers[next_num] = curr_min
            while 2*ugly_numbers[multi2] <= ugly_numbers[next_num]:  # 寻找大于已有的最后的1个丑数
                multi2 += 1
            while 3*ugly_numbers[multi3] <= ugly_numbers[next_num]:
                multi3 += 1
            while 5*ugly_numbers[multi5] <= ugly_numbers[next_num]:
                multi5 += 1
            next_num += 1
        return ugly_numbers[-1]

    # 判断一个数是不是丑数
    def IsUgly(self, num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return True if num == 1 else False


if __name__ == '__main__':
    solution = Solution()
    index1 = 5
    index2 = 0
    index3 = 1500
    print(solution.GetUglyNumber_Solution2(index1))
    print(solution.GetUglyNumber_Solution2(index1))
    print(solution.GetUglyNumber_Solution2(index1))