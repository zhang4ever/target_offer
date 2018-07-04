#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : KthNodeFromEnd.py
# @Time    : 2018-04-03 09:46
# @Author  : zhang bo
# @Note    : 链表中的倒数第k个节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    题目要求：输入一个链表， 输出该链表的倒数第k个节点
    """
    def FindKthToTail(self, head, k):
        """
        倒数第k个么就是正数的第(N-K+1)个。设置两个指针，初始时，front指向 (k-1), behind指向第1个(两个指针相距 k-1)；然后两个
        一起向前移动。当front到达链表结尾时front=n，behind刚好像指向第(n-k+1)
        """
        if head is None or k <= 0:
            return None

        node_front = head
        for i in range(k-1):  # front移动k-1
            if node_front.next is not None:  # 防止k大于链表的长度
                node_front = node_front.next
            else:
                return None

        node_behind = head
        while node_front.next is not None:  # 直到behind到达末尾
            node_front = node_front.next
            node_behind = node_behind.next

        return node_behind

    # 拓展：求链表的中间节点
    def FindKthToMiddel(self, head):
        """
        题目要求：求链表的中间节点。如果长度是奇数，返回中间节点；是偶数的时候，返回中间两个的任意一个
        思路：设置两个节点，slow和fast。他们从同一节点出发，slow每次走一步，fast一次走两步。当fast走到末尾时，slow刚好到中间
        """
        if head is None:
            return None
        node_slow = head
        node_fast = head
        while node_fast.next is not None and node_fast.next.next is not None:
            node_fast = node_fast.next.next  # fast走两步
            node_slow = node_slow.next  # slow走一步
        return node_slow

    # 拓展：判断一个链表是否有环
    def isListlinkACircle(self, head):
        """
        题目要求：判断一个链表是否有环
        思路：设置两个节点，slow和fast。他们从同一节点出发，slow每次走一步，fast一次走两步。当fast与slow相遇时则是
        """
        if head is None:
            return None
        node_slow = head
        node_fast = head
        is_circle = False
        while node_fast.next is not None and node_fast.next.next is not None:
            node_fast = node_fast.next.next  # fast走两步
            node_slow = node_slow.next  # slow走一步
            if node_fast == node_slow:
                is_circle = True
                break
        return is_circle

if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    node_res = solution.FindKthToTail(head, k=7)  # test func1
    node_res = solution.FindKthToMiddel(head)  # test func2
    if node_res is not None:
        print(node_res.val)
    node4.next = head  # test isListlinkACircle()
    print(solution.isListlinkACircle(head))  # test


