#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SerializeBinaryTrees.py
# @Time    : 2018-07-19 15:42
# @Author  : zhang bo
# @Note    : 序列化二叉树
"""
'''
题目描述：请实现两个函数，分别用来序列化和反序列化二叉树
思路：1。先序遍历树，将叶子节点的孩子用#表示。2.反序列
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 使用先序遍历进行序列化
    def Serialize(self, root):
        res = []
        if not res:
            return res
        def PreOerder(pRoot, res):  #先序
            if not pRoot:
                res.append('#')
                return
            res.append(pRoot.val)
            PreOerder(pRoot.left, res)
            PreOerder(pRoot.right, res)
            return res
        return PreOerder(root, res)

    def Deserialize(self, s):
        tree, sp = self.deserialize(s, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == "#":
            return None, sp+1
        node = TreeNode(s[sp])
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(3)
    node4, node5, node6 = TreeNode(4), TreeNode(5), TreeNode(6)
    node1.left, node1.right = node2, node3
    node2.left = node4
    node3.left, node3.right = node5, node6
    s = solution.Serialize(node1)
    print(s)
    root = solution.Deserialize(s)
    print(solution.Serialize(root))
