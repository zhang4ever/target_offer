#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : FirstCommonNodesInLists.py
# @Time    : 2018-07-08 14:27
# @Author  : zhang bo
# @Note    : 两个链表的第一个公共节点
"""
'''
题目描述：输入两个链表，找出它们的第一个公共结点。
思路1：暴力法。在第一个链表上遍历，每次遍历一个节点，在另外一个链表上顺序遍历，如果两个节点一样，则找到第一个公共的节点。时间复杂度O(mn)
思路2：单项链表有公共节点，说明公共节点出现在尾部，且从公共节点开始都是一样的，可以从尾部遍历直到遇到不一样的。考虑到后进先出，使用栈来处理。
      分别将两个链表添加到栈中，然后从栈顶依次比较，直到最后一个不一样的。时间复杂度和空间复杂度均是O(m+n).
思路3：更简单的解法，不需要借助辅助栈.先比较良好个链表的长度，先让长的链表先遍历，然后在同时遍历两个一样长的链表，直到找到相同的。O(m+n)
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 解法1：使用两个辅助栈。O(m+n)
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2.val)
            pHead2 = pHead2.next
        ans = 0
        while stack1[-1] == stack2[-1]:
            ans = stack1[-1]
            stack1.pop()
            stack2.pop()
        while pHead1.val != ans:
            pHead1 = pHead1.next
        return pHead1

    # 解法2：表较长短后同时遍历
    def FindFirstCommonNode2(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return
        length1 = self.GetListsLength(pHead1)
        length2 = self.GetListsLength(pHead2)
        long, short = (pHead1, pHead2) if length1 >= length2 else (pHead2, pHead1)
        for _ in range(abs(length1-length2)):  # 长者先行
            long = long.next
        while long and short and long != short:
            long = long.next
            short = short.next
        return long

    # 获取链表的长度
    def GetListsLength(self, node):
        length = 0
        while node:
            node = node.next
            length += 1
        return length


if __name__ == '__main__':
    solution = Solution()
    # list1:{1,2,3,6,7}; list2:{4,5,6,7}
    node11, node12, node13, node14, node15 = ListNode(1), ListNode(2), ListNode(3), ListNode(6), ListNode(7)
    node11.next, node12.next, node13.next, node14.next = node12, node13, node14, node15
    node21, node22 = ListNode(4), ListNode(5)
    node21.next, node22.next = node22, node14
    # print(solution.FindFirstCommonNode(node11, node21))
    print(solution.FindFirstCommonNode2(node11, node21).val)