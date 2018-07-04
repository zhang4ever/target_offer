#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : CopyComplextlist.py
# @Time    : 2018-04-10 09:54
# @Author  : zhang bo
# @Note    : 复制复杂链表
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x  # value
        self.next = None  # 指向下一节点
        self.random = None  # 指向人任意节点

class Solution:
    """
    要求：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
            返回结果为复制后复杂链表的head。
    思路：分三步，先依次赋值原链表上的节点，使用next链接；然后再设置random指针；最后将复制后的链表分离。
    复杂度：O(n)的时间复杂度，而且不增加额外的辅助空间
    """
    def Clone(self, pHead):
        # 第一步，将复制后的节点N'添加到源节点N的后面
        if not pHead:
            return None
        p_node = pHead  # 原始节点
        while p_node:
            cloned_node = RandomListNode(0)  # 复制后的链表
            cloned_node.label = p_node.label
            cloned_node.next = p_node.next
            cloned_node.random = None

            p_node.next = cloned_node
            p_node = cloned_node.next

        # 第二步：重新设置复制后的链表的random指针
        p_node = pHead  #
        while p_node:
            cloned_node = p_node.next  # 找到复制后的节点
            if p_node.random:  # 原节点有random指针
                cloned_node.random = p_node.random.next
            p_node = cloned_node.next

        # 第三步：将原链表和复制后的链表拆开
        p_node = pHead
        # 初始化分开后的两个链表的指针
        if p_node:
            cloned_head = cloned_node = p_node.next
            p_node.next = cloned_node.next
            p_node = p_node.next
        while p_node:
            cloned_node.next = p_node.next
            cloned_node = cloned_node.next
            p_node.next = cloned_node.next
            p_node = p_node.next
        return cloned_head


if __name__ == '__main__':
    solution = Solution()
    head = RandomListNode('A')
    node1 = RandomListNode('B')
    node2 = RandomListNode('C')
    node3 = RandomListNode('D')
    node4 = RandomListNode('E')
    head.next = node1
    head.random = node2
    node1.next = node2
    node1.random = node4
    node2.next = node3
    node3.next = node4
    node3.random = node1
    cloned = solution.Clone(head)
    print(cloned.label)
    print(cloned.next.label)
    print(cloned.next.next.label)
    print(cloned.next.next.next.label)
    print(cloned.random.label)
    print(cloned.next.random.label)
    
