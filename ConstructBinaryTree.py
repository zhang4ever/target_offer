#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ContructBinaryTree.py
# @Time    : 2018-03-24 21:52
# @Author  : zhang bo
# @Note    : 
"""
'''
描述:输入某二叉树的前序遍历要和中序遍历，。请重构出该二叉树。假设输入的前序和中序的结果都不含重复的数字。
思路：先根据前序的第一个数字确定头结点，然后根据中序遍历确定头结点的位置，从而确定左右子树的数量，然后使用递归的思想。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        if set(pre) != set(tin):  # 确保先序遍历和中序遍历的数字是一致的
            print('invalid input!')
            return None
        # 确定头结点：前序遍历结果中的第一个数
        root_val = pre[0]
        root = TreeNode(root_val)  # 建立树的头结点
        pos = tin.index(root_val)  # 头结点在中序遍历结果中的位置
        root.left = self.reConstructBinaryTree(pre[1: pos + 1], tin[0: pos])  # 用头节点以前的构造左子树
        root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])  # 用头节点以后的构造右子树
        return root

    # 前序遍历（递归）
    def printTreeByPreorder(self, root):

        res = []
        def Preorder(root, res):
            if root is None:
                return None
            # print(root.val)
            res.append(root.val)
            Preorder(root.left, res)
            Preorder(root.right, res)
            return res
        return Preorder(root, res)

    # 中序遍历（递归）
    def printTreeByInorder(self, root):

        res = []
        def Inorder(root, res):
            if root is None:
                return None
            Inorder(root.left, res)
            # print(root.val)
            res.append(root.val)
            Inorder(root.right, res)
            return res
        return Inorder(root, res)

    # 后序遍历(递归)
    def printTreeByPosterorder(self, root):

        res = []
        def Posterorder(root, res):
            if root is None:
                return None
            Posterorder(root.left, res)
            Posterorder(root.right, res)
            # print(root.val)
            res.append(root.val)
            return res
        return Posterorder(root, res)

    #层序遍历
    def printTreeByLevel(self, root):
        if root is None:
            return None
        res = []
        stack = [root]
        while stack:
            current = stack.pop()
            # print(current.val, stack)
            res.append(current.val)
            if current.left:
                stack.insert(0, current.left)
            if current.right:
                stack.insert(0, current.right)
        return res


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    pre1 = tin1 = []
    pre2 = tin2 = [1]
    print('original pre:%s' % pre)
    print('original tin:%s' % tin)
    solution = Solution()
    root = solution.reConstructBinaryTree(pre, tin)
    print('pre:%s' % solution.printTreeByPreorder(root))
    print('tin:%s' % solution.printTreeByInorder(root))
    print('poster:%s' % solution.printTreeByPosterorder(root))
    print('level:%s' % solution.printTreeByLevel(root))
