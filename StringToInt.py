#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : StringToInt.py
# @Time    : 2018-07-13 17:15
# @Author  : zhang bo
# @Note    : 将一个字符串转化成一个Int
"""
'''
题目本身不难，但是需要考虑到各种边界值很非法输入：当第一个是“+”或者“-”， “0” 
'''
class Solution:
    def StrToInt(self, s):
        if not s or len(s) < 1:
            return 0
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        res_stack = []
        for i in s:
            if i in num_dict.keys():
                res_stack.append(num_dict[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0  # 中间有非法字符

        if len(res_stack) == 1 and res_stack[0] == 0:
            return 0
        ans = 0
        for i in res_stack:
            ans = ans * 10 + i
        if s[0] == '-':
            ans = -ans
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = '209'
    s = '+209'
    s = '-209'
    s = ''
    s = '20-9+8'
    print(solution.StrToInt(s))