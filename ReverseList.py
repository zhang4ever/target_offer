#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseList.py
# @Time    : 2018-04-03 13:40
# @Author  : zhang bo
# @Note    : 反转列表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    要求：输入一个链表，反转链表后，输出链表的所有元素。
    思路：原链表的头变成反转后的链表的尾；原链表的尾变成翻转后的链表的头；
    """
    def ReverseList(self, pHead):
        p_reverse_head = None  # 反转后的节点
        p_node = pHead  # 当前节点
        p_prev = None   # 原链表的前一个节点
        while p_node is not None:
            p_next = p_node.next
            if p_next is None:  # 原链表没有下一个节点：
                p_reverse_head = p_node
            p_node.next = p_prev  # 尾
            p_prev = p_node
            p_node = p_next
        return p_reverse_head

    #  递归实现
    def ReverseList2(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        else:
            reversed_head = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return reversed_head


def printList(head):
    while head is not None:
        print(head.val, end='->')
        head = head.next
    print('\t')


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    print('original list:')
    printList(head)
    solution = Solution()
    head_reversed = solution.ReverseList2(head)
    print('reversed list：')
    printList(head_reversed)

