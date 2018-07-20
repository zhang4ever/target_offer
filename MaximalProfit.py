#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MaximalProfit.py
# @Time    : 2018-07-20 11:30
# @Author  : zhang bo
# @Note    : 股票的最大利润
"""

'''
题目描述：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的利润是多少？
示例：一只股票在某些时间节点的价格是{9,11,8,5,7,12,16,14}。如果我们能在价格为5的时候买入并在价格为16的时候卖出，则能收获最大利润11。
思路：遍历数组时，每次记录当前的已经遍历过的最小值，同时计算以该最小值买入时当前遍历到的价格卖出时收益diff，
    最后返回最大的diff就是所能获得的最大收益。
'''

class Solution:
    def MaxDiff(self, numbers):
        min_price = numbers[0]
        max_diff = numbers[1] - min_price
        buy_sale = {'buy': min_price, 'sale': numbers[1]}
        for i in range(2, len(numbers)):
            if numbers[i] < min_price:
                min_price = numbers[i]
            curr_diff = numbers[i] - min_price
            if max_diff < curr_diff:
                max_diff = curr_diff
                buy_sale['buy'] = min_price
                buy_sale['sale'] = numbers[i]
        return max_diff, buy_sale


if __name__ == '__main__':
    solution = Solution()
    numbers = [9, 11, 8, 5, 7, 12, 16, 14]
    print(solution.MaxDiff(numbers))
