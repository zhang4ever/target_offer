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

    '''
    拓展：判断一个二叉树是不是平衡二叉树(任意节点的左右子树的深度差不超过1).
    思路1:遍历每个节点的时候，调用deep的函数来计算以该节点为head的深度。
    '''

    # 该方法的缺点就是每个节点都会重复遍历好多次,时间效率不高
    def IsBalanced(self, pRoot):
        if not pRoot:
            return True
        # 遍历没和节点
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        if abs(left_depth-right_depth) > 1:
            return False
        return self.IsBalanced(pRoot.left) and self.IsBalanced(pRoot.right)

    # 改进的方法：
    def IsBalanced2(self, pRoot, depth=0):
        if not pRoot:
            depth = 0
            return True
        left = self.IsBalanced2(pRoot.left, depth)
        right = self.IsBalanced2(pRoot.right, depth)
        if abs(left - right) < 1:
            if left > right:
                depth = 1 + left
            else:
                depth + 1 + right
            return True
        return False


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
    print(solution.IsBalanced2(root))