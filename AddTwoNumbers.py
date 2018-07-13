#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : AddTwoNumbers.py
# @Time    : 2018-07-13 16:01
# @Author  : zhang bo
# @Note    : 不用加减乘除做加法
"""
'''
题目描述：写一个函数，求两个整数之和，要求在那函数体内不得使用加减乘除四则运算符
思路1：使用二进制来模拟加法的运算：先将每一位相加， 不计进位；然后记录进位的结果；最后将两个结果相加。这里加可以使用异或来代替;
思路2：使用递归。求出两个数相加时需要进位的和不需要进位的，如果两个没有重合，返回他们的或；否则递归。
'''
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            add = num1 ^ num2  # 加
            carry = (num1 & num2) << 1  # 需要进位
            num1 = add
            num2 = carry
        return num1

    def Add2(self, num1, num2):
        temp1 = (num1 & num2) << 1  # 需要进位的
        temp2 = num1 ^ num2  # 不需要进位的
        if temp1 & temp2 == 0:
            return temp1 | temp2
        else:
            return self.Add(temp1, temp2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.Add(5, 7))
    print(solution.Add2(5, 7))