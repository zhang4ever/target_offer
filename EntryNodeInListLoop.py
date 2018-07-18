#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : EntryNodeInListLoop.py
# @Time    : 2018-07-18 15:35
# @Author  : zhang bo
# @Note    : 链表中环的入口节点
"""
'''
题目描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：先判断链表中是否有环（两个指针同时从头节点出发，慢的走一步，快的走两步，如果慢的追上快的则存在），然后找入口（找到环中的
    任何一个节点就可以得到环中节点的数目，然后两个指针同时从头节点出发，快的先走N步，满的走一步，相遇的节点就是入口）
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return
        meetingNode = self.GetMeetingNode(pHead)  # 是否有环，有就返回环中的一个节点
        if not meetingNode:
            return None
        # 首先获取环的节点的数量
        num_in_loop = 1
        pNode = meetingNode
        while pNode.next != meetingNode:
            num_in_loop += 1
            pNode = pNode.next
        # 寻找入口
        slow, fast = pHead, pHead  # 两个节点同时从头节点出发
        for _ in range(num_in_loop):  # 快的先走N步
            fast = fast.next
        while slow != fast:  # 两个指针同频率走，直到相遇
            slow = slow.next
            fast = fast.next
        return fast

    # 判断一个链表是否有环，有就返回其后的一个节点，没有None
    def GetMeetingNode(self, pHead):
        slow, fast = pHead, pHead
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            if slow == fast:
                return fast
        return


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
    node4, node5, node6 = ListNode(4), ListNode(5), ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    print(solution.GetMeetingNode(node1).val)  # 判断有没有环
    print(solution.EntryNodeOfLoop(node1).val)  # 入口
