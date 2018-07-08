#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PrintListReversing_Recursively.py
# @Time    : 2018-03-23 19:33
# @Author  : zhang bo
# @Note    : 逆序打印链表
"""
'''
描述：输入一个链表的头结点，从尾到头打印
思路：先顺序遍历链表的所有节点，然后入栈，最后在出栈就会得到逆序的结果
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    # 1. 直接使用递归
    def printListFromTailToHead1(self, listNode):
        # write code here
        if ListNode is not None:
            if listNode.next is not None:
                self.printListFromTailToHead1(listNode.next)
        print(listNode.val)
        return listNode.val


    # 使用栈来处理
    def printListFromTailToHead2(self, listNode):

        res = []
        if listNode is None:
            return res
        while listNode is not None:
            res.insert(0, listNode.val)  # insert的魅力， 入栈
            listNode = listNode.next
        return res


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node4 = ListNode()
    node5 = ListNode(5)
    solution = Solution()
    print(solution.printListFromTailToHead2(node4))
