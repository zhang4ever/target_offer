#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : BalancedBinaryTree.py
# @Time    : 2018-07-08 21:28
# @Author  : zhang bo
# @Note    : 平衡二叉树
"""
'''
    描述：判断一个二叉树是不是平衡二叉树(任意节点的左右子树的深度差不超过1).
    思路1:遍历每个节点的时候，调用deep的函数来计算以该节点为head的深度。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = True

    # 解法1：该方法的缺点就是每个节点都会重复遍历好多次,时间效率不高
    def IsBalanced_solution(self, pRoot):
        if not pRoot:
            return True
        # 遍历没和节点
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return self.IsBalanced_solution(pRoot.left) and self.IsBalanced_solution(pRoot.right)

    # 解法2：每个节点只遍历一次
    def IsBalanced_Solution2(self, pRoot):
        self.IsBalanced(pRoot)
        return self.flag

    def IsBalanced(self, pRoot):
        if not pRoot:
            self.flag = True
            return 0
        left = 1 + self.IsBalanced(pRoot.left)
        right = 1 + self.IsBalanced(pRoot.right)
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right)

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
    print(solution.IsBalanced_Solution2(root))