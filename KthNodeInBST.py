#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : KthNodeInBST.py
# @Time    : 2018-07-16 11:25
# @Author  : zhang bo
# @Note    : 二叉搜索树的第K大节点
"""

'''
题目描述：给定一颗二叉搜索树，请找出其中的第k小的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
思路：其实考察的就是二叉树的中序遍历，然后第k和节点就是。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def KthNode(self, pRoot, k):
        """
        :return: 返回对应节点TreeNode
        """

        if not pRoot or k == 0:
            return
        res = []
        self.KthNodeCore(pRoot, res)
        return res[k-1] if 0 <= k <= len(res) else None

    def KthNodeCore(self, pRoot, res):
        if not pRoot:
            return
        if pRoot.left:
            self.KthNodeCore(pRoot.left, res)
        res.append(pRoot)
        if pRoot.right:
            self.KthNodeCore(pRoot.right, res)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    node2, node3 = TreeNode(3), TreeNode(7)
    node4, node5 = TreeNode(2), TreeNode(4)
    node6, node7 = TreeNode(6), TreeNode(8)
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    root.left, root.right = node2, node3
    k = 3
    print(solution.KthNode(root, k).val)