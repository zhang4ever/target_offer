#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MirrorOfBinaryTree.py
# @Time    : 2018-04-07 20:51
# @Author  : zhang bo
# @Note    : 二叉树的镜像问题
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题目要求：操作给定的二叉树，将其变换为源二叉树的镜像。
    思路：二叉树的镜像就是保持根节点不便，然后左子树和右子树交换位置。所以思路就是：先先序遍历二叉树，如果有子树，那么将左右子树互换位置
    """
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return None
        # 交换左右子树
        root.left, root.right = root.right, root.left
        # 在根节点的每层左右子树进行相同的操作
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root

    # 循环法：使用栈
    def Mirror2(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            tree = stack[-1]
            stack.pop()
            if tree.left or tree.right:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:  # 交换完后， tree左子树不为空（空就不管）
                stack.insert(0, tree.left)
            if tree.right:  # 交换完后， tree右子树不为空（空就不管）
                stack.insert(0, tree.right)
        return root


#层序遍历
def printTreeByLevel(root):
    if root is None:
        return None
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        res.append(current.val)
        if current.left:
            stack.insert(0, current.left)
        if current.right:
            stack.insert(0, current.right)
    return res


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(10)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node5 = TreeNode(9)
    node6 = TreeNode(11)
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    root.left = node1
    root.right = node2
    print(printTreeByLevel(root))
    print(printTreeByLevel(solution.Mirror(root)))
    print(printTreeByLevel(root))

