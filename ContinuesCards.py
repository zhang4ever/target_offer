#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ContinuesCards.py
# @Time    : 2018-07-11 22:56
# @Author  : zhang bo
# @Note    : 扑克牌的顺子
"""
'''
题目描述：从扑克牌中随机抽取5张，判断是不是一个顺子，即5张牌是不是连续的。2到10为数字版本身，A为1，J为11，Q为12，K为13，而大小王
        可以看作是任意数字看作是任意数字。
思路：首先将数组进行排序，在统计其中的0的个数，最后统计排序后的数组中相邻的数字之间的空缺的数目，如果空缺的数目小于0的数目，则这个数组
    就是连续的；否在不是连续的。还有一种情况就是，如果数组中间有重复的数字，即如果有对子存在，则说明不可能有顺子存在。
    
'''

class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) < 5:
            return False
        numbers.sort()
        num_0, num_gap = 0, 0
        for i in range(len(numbers)):  # count 0
            if numbers[i] == 0:
                num_0 += 1
        small = num_0
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:  # 出现对子了
                return
            num_gap += (numbers[big] - numbers[small] - 1)
            small = big
            big += 1
        return True if num_gap <= num_0 else False


if __name__ == '__main__':
    solution = Solution()
    numbers1 = [1, 3, 2, 5, 4]
    numbers2 = [1, 2, 3, 4]
    numbers3 = [1, 2, 3, 4, 0]
    numbers3 = [1, 2, 5, 6, 0]
    print(solution.IsContinuous(numbers1))
    print(solution.IsContinuous(numbers2))
    print(solution.IsContinuous(numbers3))
