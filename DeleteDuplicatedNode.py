#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : DeleteDuplicatedNode.py
# @Time    : 2018-07-18 09:09
# @Author  : zhang bo
# @Note    : 删除链表中的重复节点
"""

'''
题目描述：在一个排序的链表中，如何删除重复的节点。
思路：只要判断当前节点与下一节点的val是否相等。记录重复的节点的前置节点，然后删除重复的后，将前置接点的下一节点指向比重复节点大的节点即可。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return
        pPreNode = None  # 当前节点的前置界定啊
        pNode = pHead  # 当前
        while pNode:
            needDelete = False  # 当前节点是否需要删除
            pNext = pNode.next
            if pNext and pNode.val == pNext.val:  # 当前节点与下一个节点重复
                needDelete = True
            if not needDelete:  # 当前节点不重复，继续遍历
                pPreNode = pNode
                pNode = pNode.next
            else:  # 当前节点与下一节点重复，删除
                value = pNode.val  # 记录要删除的值
                pToBeDeleted = pNode
                while pToBeDeleted and pToBeDeleted.val == value:
                    pToBeDeleted = pToBeDeleted.next
                if not pPreNode:  # 如果头节点也是重复的，删除后要重新确定头
                    pHead = pToBeDeleted
                else:
                    pPreNode.next = pToBeDeleted  #
                pNode = pToBeDeleted
        return pHead


def printList(pHead):
    while pHead:
        print(pHead.val, end='->')
        pHead = pHead.next
    print('', end='\n')


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
    node4, node5 = ListNode(3), ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    printList(node1)
    node1 = solution.deleteDuplication(node1)

    printList(node1)

