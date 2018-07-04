#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MergeList.py
# @Time    : 2018-04-05 16:07
# @Author  : zhang bo
# @Note    : 合并两个排序的链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    要求：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
    思路：先确定合并后链表的节点。由于是升序，所以两个链表的都节点小的作为合并后的头结点；
        确定了都节点后没，再将剩下的节点做类似的操作。所以该问题是递归的。
    """

    # 递归
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            mergedHead = pHead1
            mergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            mergedHead = pHead2
            mergedHead.next = self.Merge(pHead1, pHead2.next)
        return mergedHead


def printList(head):
    while head is not None:
        print(head.val, end='->')
        head = head.next
    print('\t')


if __name__ == '__main__':
    solution = Solution()
    head1 = ListNode(1)
    head2 = ListNode(2)
    node1 = ListNode(3)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node4 = ListNode(6)
    node5 = ListNode(7)
    node6 = ListNode(8)
    head1.next = node1
    node1.next = node3
    node3.next = node5
    head2.next = node2
    node2.next = node4
    node4.next = node6
    # head1 = None
    # head2 = None
    print("linklist1:\t")
    printList(head1)
    print("linklist2:\t")
    printList(head2)
    print('mergedlist1:\t')
    printList(solution.Merge(head1, head2))
