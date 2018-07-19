#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PrintTreesFromTopToBottom.py
# @Time    : 2018-04-09 09:47
# @Author  : zhang bo
# @Note    : 二叉树的层序遍历
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    """
    从上往下打印出二叉树的每个节点，同层节点从左至右打印。
    思路：使用队列。先将头节点加入队列， 然后打印头节点，将头节点出队列，并将头节点的左孩子和右孩子以此加入队列。
    """
    def PrintFromTopToBottom(self, root):
        if not root:
            return None
        queue = [root]
        res = []
        while queue:
            current = queue.pop()
            res.append(current.val)
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
        return res


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(10)
    root.left = node1
    root.right = node2
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node1.left = node3
    node1.right = node4
    node5 = TreeNode(9)
    node6 = TreeNode(11)
    node2.left = node5
    node2.right = node6
    print(solution.PrintFromTopToBottom(root))
