#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MinInStack.py
# @Time    : 2018-04-08 14:15
# @Author  : zhang bo
# @Note    : 包含min函数的栈
"""

class Solution:
    """
    题目要求：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
            在该栈中，调用pop,push ,top的时间复杂度都是O(1)

    思路：建立一个辅助栈，用来存放最小的（次小的元素）。没压入一个元素是，便往辅助栈里面压入一个当前最小的元素。出栈时，辅助栈也跟着出栈。

    """

    def __init__(self):
        self.stack = []  # 数据栈
        self.min_stack = []  # 辅助栈

    def push(self, node):

        self.stack.append(node)  # 数据栈push
        if len(self.min_stack) == 0 or node < self.top():
            self.min_stack.append(node)  # 辅助栈中push最小值
        else:
            self.min_stack.append(self.top())  # 如果node的值较大，则将数据栈的top值插入

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.min_stack[-1]

    def min(self):
        if len(self.min_stack) > 0:
            return self.top()


if __name__ == '__main__':
    solution = Solution()
    solution.push(3)
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))
    solution.push(4)
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))
    solution.push(2)
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))
    solution.push(1)
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))
    solution.pop()
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))
    solution.pop()
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))
    solution.push(0)
    print('stack：%s, min_stack：%s, min:%s' % (solution.stack, solution.min_stack, solution.min()))

    
