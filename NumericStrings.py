#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NumericStrings.py
# @Time    : 2018-07-18 13:03
# @Author  : zhang bo
# @Note    : 表示数值的字符串
"""

'''
题目描述：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
        例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
根据指数字符E的特殊性。他只能出现在小数点的后面，并且E的前后的第0位都有可能是+-号，所以将原始的字符以E分割成两半，然后对两半分别进行扫描。
'''

class Solution:
    # s字符串
    def isNumeric(self, s):
        if not s or len(s) == 0:
            return False
        s = s.lower()
        if 'e' in s:  # 以E分割的原因是E的左边第0位和E的右边的第0位都可以有+=号
            pos = s.index('e')
            left = s[:pos]
            right = s[pos+1:]
            # E后面不能什么都没有，点只能出现在E的左边
            if len(right) == 0 or '.' in right:
                return False
            isNumeric = self.scanDigits(left) and self.scanDigits(right)
        else:
            isNumeric = self.scanDigits(s)
        return isNumeric


    def scanDigits(self, s):
        res_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', 'e', '.']  # 合法的字符集
        ch_num = {'e': 0, '.': 0}
        for i in range(len(s)):
            if s[i] not in res_list:
                return False
            if s[i] == '.':
                ch_num['.'] += 1
            if s[i] == 'e':
                ch_num['e'] += 1
            if s[i] in '+-' and i != 0:
                return False
        if ch_num['.'] > 1 or ch_num['e'] > 1:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = '1a3.14'
    s = '+55e'
    s = '12e+4.3'
    s = '123.45e+6'
    print(solution.isNumeric(s))