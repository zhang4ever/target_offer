#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NextNodeInBinaryTrees.py
# @Time    : 2018-07-16 21:54
# @Author  : zhang bo
# @Note    : 二叉树的下一个节点
"""
'''
题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，
        同时包含指向父结点的指针。
思路：由于是中序遍历，所以只要考虑右子树的遍历即可。分两种情况，有右子树和无右子树两种情况。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        pNext = None
        # 1、该节点有右右子树， 则找到该右子树的最左孩子
        if pNode.right:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left
            pNext = pRight  # 找到
        # 2、该节点没有右子树，而且是父节点的右孩子
        elif pNode.next:
            current = pNode
            pParent = pNode.next
            while pParent and current == pParent.right:
                current = pParent
                pParent = current.next
            pNext = pParent
        return pNext


if __name__ == '__main__':
    solution = Solution()
    node_a, node_b, node_c = TreeLinkNode('a'), TreeLinkNode('b'), TreeLinkNode('c')
    node_d, node_e, node_f = TreeLinkNode('d'), TreeLinkNode('e'), TreeLinkNode('f')
    node_a.left, node_a.right = node_b, node_c
    node_b.left, node_b.right, node_b.next = node_d, node_e, node_a
    node_c.next = node_a
    node_d.next, node_e.next = node_b, node_b
    print(solution.GetNext(node_d))
