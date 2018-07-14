#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ContinuesSequenceWithSum.py
# @Time    : 2018-07-09 16:14
# @Author  : zhang bo
# @Note    : 和为s的连续的正数序列
"""
'''
题目描述：输入一个正数s,打印出所有和为s的连续正数序列（至少两个数）。
示例：例如输入15, 输出{(1,2,3,4,5), (4,5,6), (7,8)}
思路1：设置两个标志small和big来记录当前子序列的最小值(初始为1,2)。sum(small, big)大于tsum, small+1;
      如果小于，big+1;如果等于，print同时big+1;       
'''

class Solution:
    # O(n)
    def FindContinuousSequence(self, tsum):
        if tsum <= 3:
            return []
        small = 1
        big = 2
        middle = (1 + tsum) // 2
        curr_sum = small + big
        res = []
        while small < middle:  # 如果当small大于中值，那么big+small势必会大于tsum, 没有意义
            if curr_sum == tsum:  # 刚好找到
                res.append(self.SaveContinuousSequence(small, big))
            while curr_sum > tsum and small < middle:  # 发现大了，所以丢弃最前面的较小值，直到等于tsum
                curr_sum -= small
                small += 1
                if curr_sum == tsum:
                    res.append(self.SaveContinuousSequence(small, big))
            big += 1
            curr_sum += big
        return res

    def SaveContinuousSequence(self, small, big):
        res = [x for x in range(small, big + 1)]
        return res


if __name__ == '__main__':
    solution = Solution()
    tsum = 9
    print(solution.FindContinuousSequence(tsum))

