#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SortArrayForMinNumber.py
# @Time    : 2018-07-05 16:17
# @Author  : zhang bo
# @Note    : 把数组排列成最小的数
"""
'''
题目描述:输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例：例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路1：使用排列组合。先对数组进行全排列，然后选择最小的组合。O(nlogn)
思路2：通过新定义排序规则; 时间复杂度O(nlogn)
'''

class Solution:

    # 解法1：使用全排列组合法，时间复杂度O(nlogn)
    def PrintMinNumber(self, numbers):
        if not numbers:
            return
        group_list = self.group_array(numbers)  # 全排组合
        res = []
        for l in group_list:
            tmp = ''.join(str(i) for i in l)
            res.append(tmp)
        return min(res)

    # 解法2：定义新排序规则。时间复杂度O(nlogn)
    def PrintMinNumber2(self, numbers):
        if not numbers:
            return ''
        from functools import cmp_to_key
        num_list = []
        for i in range(len(numbers)):
            num_list.append(str(numbers[i]))
        key = cmp_to_key(lambda x, y: int(x+y) - int(y+x))
        num_list.sort(key=key)
        return ''.join(num_list)

    # 对一个数组进行全排列
    def group_array(self, array):
        if not array:
            return
        if len(array) == 1:
            return [array]
        res = []
        for i in range(len(array)):
            if i > 0 and array[i] == array[i - 1]:
                continue
            temps = self.group_array(array[0:i] + array[i + 1:])
            for j in temps:
                res.append([array[i]] + j)
        return res


if __name__ == '__main__':
    solution = Solution()
    numbers = [3, 32, 321]
    numbers = []
    numbers = [3]
    print(solution.PrintMinNumber(numbers))