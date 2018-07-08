#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : TreeDepth.py
# @Time    : 2018-07-08 19:32
# @Author  : zhang bo
# @Note    : 二叉树的深度
"""
'''
题目描述：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
思路1：递归。只有头节点，deep=1;如果只有左子树，deep=deep(左子树)+1；如果只有右子树，deep=deep(右子树)+1；如果左子树和右子树都有；
      deep=max(deep(左子树),deep(右子树))+1.时间复杂度O(n)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 使用递归的思路.时间O(n),空间O(logn)
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        return left_depth + 1 if left_depth > right_depth else right_depth + 1


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    node1, node2, node3 = TreeNode(2), TreeNode(3), TreeNode(4),
    node4, node5, node6 = TreeNode(5), TreeNode(6), TreeNode(7)
    root.left, root.right = node1, node2
    node1.left, node1.right = node3, node4
    node2.right = node5
    node4.left = node6
    print(solution.TreeDepth(root))