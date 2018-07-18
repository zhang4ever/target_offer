#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SymmetricalBinaryTree.py
# @Time    : 2018-07-18 20:22
# @Author  : zhang bo
# @Note    : 对称的二叉树
"""

'''
题目描述：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
思路：如果一个树的的先序遍历(上左右)和对称的先序遍历(上右左)的序列是一样的，说明就是对称的，
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalCore(pRoot, pRoot)

    def isSymmetricalCore(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        ans1 = self.isSymmetricalCore(pRoot1.left, pRoot2.right)
        ans2 = self.isSymmetricalCore(pRoot1.right, pRoot2.left)
        return ans1 and ans2


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = TreeNode(8), TreeNode(6), TreeNode(6)
    node4, node5 = TreeNode(5), TreeNode(7)
    node6, node7 = TreeNode(7), TreeNode(5)
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node1.left, node1.right = node2, node3
    # node1 = None
    print(solution.isSymmetrical(node1))

