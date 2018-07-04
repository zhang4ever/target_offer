#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : DeleteNodeInList.py
# @Time    : 2018-04-01 22:28
# @Author  : zhang bo
# @Note    : 删除链表节点
"""
import time

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    """
    题目描述：给定单向链表的头结点和一个要删除的结点，定义一个函数在O(1)时间内删除该节点
    """
    # 常规方法，顺序查找
    def delete_node1(self, head, node_deleted):
        if head is None:
            return None
        p_node = head
        while p_node != node_deleted:
            p_node = p_node.next
        p_node.__del__()
        node_deleted.__del__()

    def delete_node2(self, head, node_deleted):
        """
        考虑三种情况：删除的是尾节点、删除的是头结点、删除的是一般节点
        """
        if not head or not node_deleted:  # 头结点为空或者要删除的为空
            return None
        # 1. 要删除的节点不是尾节点
        if node_deleted.next is not None:
            tmp_node = node_deleted.next
            node_deleted.val = tmp_node.val
            node_deleted.next = tmp_node.next
            tmp_node.__del__()
        # 2. 要删除的节点只有一个节点
        elif head == node_deleted:
            head.__del__()
        # 3. 链表有多个节点，且要删除的节点是尾节点
        else:
            tmp_node = head
            while tmp_node != node_deleted:
                tmp_node = tmp_node.next
            tmp_node.next = None
            node_deleted.__del__()


def print_list(head):
    p_node = head
    while p_node is not None:
        print(p_node.val, end='->')
        p_node = p_node.next

def run_time(func, n, m):
    s1 = time.clock()
    res = func(n, m)
    e1 = time.clock()
    print('func: %s, result:%s, time: %s' % (func.__name__, res, (e1-s1)))


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print_list(head)
    print('\t')
    run_time(solution.delete_node2, head, node3)
    print_list(head)

