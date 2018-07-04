#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PathInTree.py
# @Time    : 2018-04-09 15:14
# @Author  : zhang bo
# @Note    : 二叉树中和为某一值得路径
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    要求：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下
        一直到叶结点所经过的结点形成一条路径。
    思路：使用先序遍历来遍历二叉树（因为路径是从root节点出发）。如果遍历到叶节点后。路径里面的和刚好==expectNumber，则打印该条记录。
    然后回退到上衣root节点，继续遍历。----递归
    """
    # 返回二维列表，内部每个列表表示找到的路径

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if not root.left and root.right:
            if expectNumber == root.val:
                return [[root.val]]
            else:
                return []
        res_paths = []  # 记录所有找到的路径，并返回
        current_path = []  # 一个栈，记录当前正在遍历的路径
        self.findPathRecursively(root, expectNumber, current_path, res_paths)
        return res_paths


    # 还是用递归法来查找路径
    def findPathRecursively(self, root, expectNumber, current_path, res_paths):

        # 最小问题操作
        current_path.append(root.val)
        is_leaf = root.left is None and root.right is None  # 判断是否到达叶节点
        if expectNumber == sum(current_path) and is_leaf:
            # res_paths.append(current_path)  # 会返回[]
            res_paths.append(current_path[:])

        if root.left:
            self.findPathRecursively(root.left, expectNumber, current_path, res_paths)
        if root.right:
            self.findPathRecursively(root.right, expectNumber, current_path, res_paths)
        # 到达叶节点后，由于要地贵点上一层，需要将当前路径回退
        current_path.pop()


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(12)
    root.left = node1
    root.right = node2
    node3 = TreeNode(4)
    node4 = TreeNode(7)
    node1.left = node3
    node1.right = node4
    expectNumber = 22
    # root = None
    print(solution.FindPath(root, expectNumber))
