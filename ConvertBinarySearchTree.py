#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ConvertBinarySearchTree.py
# @Time    : 2018-04-10 14:54
# @Author  : zhang bo
# @Note    : 二叉搜索数与双向链表
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    # 题目:输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
    # 思路：中序遍历二叉搜索树:递归.在左子树递归时，遍历到左子树中最右节点（最大）max,让root的left指向max, max的right指向root;
            在右子树递归时，遍历到右子树的最左节点（最小）min， 让root的right指向min，min的left指向root.
    """
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        converted = self.ConvertNode(pRootOfTree)
        while converted.left:
            converted = converted.left
        return converted

    def ConvertNode(self, root):
        # 左子树递归
        if root.left:
            self.ConvertNode(root.left)
        left_max_node = root.left
        if left_max_node:
            while left_max_node.right:  # 定位到左子树的最大值
                left_max_node = left_max_node.right
            root.left = left_max_node
            left_max_node.right = root

        # 右子树递归
        if root.right:
            self.ConvertNode(root.right)
        right_min_node = root.right
        if right_min_node:
            while right_min_node.left:
                right_min_node = right_min_node.left  # 定位到右子树最小的节点
            root.right = right_min_node
            right_min_node.left = root
        return root


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    node1 = TreeNode(6)
    node2 = TreeNode(14)
    root.left = node1
    root.right = node2
    node3 = TreeNode(4)
    node4 = TreeNode(8)
    node1.left = node3
    node1.right = node4
    node5 = TreeNode(12)
    node6 = TreeNode(16)
    node2.left = node5
    node2.right = node6
    print(solution.Convert(root).left.right.val)
    # root = None
    # print(solution.Convert(root).val)
    # root = TreeNode(0)  # 测试只有一个节点
    # root.left = None
    # root.right = None
    # print(solution.Convert(root).val)
