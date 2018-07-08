#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : StackPushPopOrder.py
# @Time    : 2018-04-08 22:09
# @Author  : zhang bo
# @Note    : 栈的压入、弹出序列
"""

class Solution:
    """
    题目要求：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
            例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
    """
    def IsPopOrder(self, pushV, popV):
        is_pop_order = False
        stack = []  # 辅助栈
        next_push = 0  # 指针-压栈序列下一个压入的
        next_pop = 0  # 指针-出栈序列下一个出栈的
        while next_pop <= len(popV):  # out-while-loop start    遍历整个出栈序列
            while not stack or stack[-1] != popV[next_pop]:  # inside-while-loop start  直到栈顶的值==下一个出栈序列中的值
                if next_push == len(pushV):  # 压栈序列中的所有元素都已经入栈， break
                    break
                stack.append(pushV[next_push])
                print(stack)
                next_push += 1
            if not stack or stack[-1] != popV[next_pop]:
                break
            stack.pop()  # 如果栈顶的值==下一个出栈序列中的值， 那么出栈该元素
            print(stack)
            next_pop += 1
        if not stack and next_pop == len(popV):  # check
            is_pop_order = True
        return is_pop_order


if __name__ == '__main__':
    solution = Solution()
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 3, 5, 1, 2]
    # popV = [5, 4, 3, 2, 1]
    # pushV = []
    # popV = []
    print(solution.IsPopOrder(pushV, popV))

