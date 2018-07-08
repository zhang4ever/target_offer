#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SubstructureInTree.py
# @Time    : 2018-04-06 15:04
# @Author  : zhang bo
# @Note    : 树的子结构
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题目要求：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
    """
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:  # tree2的头结点在tree1,就比较tree1中是否有和tree2一样的结构
                result = does_tree1_has_tree2(pRoot1, pRoot2)
            # 如果tree1可能含有多个tree2的头结点
            if not result:  # 在 tree1的左子树中继续寻找
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:  # 在左子树中没有找到，继续在右子树中寻找
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

# 判断tree1中是否含有tree2一样的结构
def does_tree1_has_tree2(pRoot1, pRoot2):
    if not pRoot2:  # 此时，说明tree2每个节点已经被遍历完
        return True
    if not pRoot1:
        return False
    if pRoot1.val != pRoot2.val:  # tree1的节点与tree2的不一样
        return False
    # 分别比较tree1和tree2的左子树和右子树，如果都一样，则返回true
    return does_tree1_has_tree2(pRoot1.left, pRoot2.left) and does_tree1_has_tree2(pRoot1.right, pRoot2.right)


if __name__ == '__main__':
    solution = Solution()
    node11 = TreeNode(8)  # tree1的头结点
    node12 = TreeNode(8)
    node13 = TreeNode(7)
    node14 = TreeNode(9)
    node15 = TreeNode(2)
    node16 = TreeNode(4)
    node17 = TreeNode(7)
    node15.left = node16
    node15.right = node17
    node12.left = node14
    node12.right = node15
    node11.left = node12
    node11.right = node13
    node21 = TreeNode(8)  # tree2的头结点
    node22 = TreeNode(9)
    node23 = TreeNode(2)
    node21.left = node22
    node21.right = node23
    print(solution.HasSubtree(node11, node21))
