#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PrintTreesInZigzag.py
# @Time    : 2018-07-19 14:30
# @Author  : zhang bo
# @Note    : 按照之字形打印二叉树
"""
'''
题目描述:请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照
        从左到右的顺序打印，其他行以此类推。
思路：使用两个栈来实现。当打印奇数层的时候，按照先左后右的顺序将子节点入栈。当打印偶数层的时候，按照先右后左的顺序将子节点入栈。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res, res_curr = [], []  # 最终的结果与当前的结果

        currlevel, nextlevel = 1, 0  # 分别表示奇数层和偶数层
        stack = [[], []]  # 两个栈，分别保存当前的节点和下一层的节点。
        stack[currlevel].append(pRoot)
        while stack[0] or stack[1]:
            pop_node = stack[currlevel].pop()  # 出栈
            print(pop_node.val, end=' ')  # 打印
            res_curr.append(pop_node.val)
            if currlevel == 1:  # 奇数层, 先左后右
                if pop_node.left:
                    stack[nextlevel].append(pop_node.left)
                if pop_node.right:
                    stack[nextlevel].append(pop_node.right)
            else:  # 偶数层，先右后左
                if pop_node.right:
                    stack[nextlevel].append(pop_node.right)
                if pop_node.left:
                    stack[nextlevel].append(pop_node.left)

            # 换行打印
            if len(stack[currlevel]) == 0:  # 当前层全部出栈
                print('', end='\n')
                res.append(res_curr)
                currlevel = 1 - currlevel
                nextlevel = 1 - nextlevel
                res_curr = []
        del res_curr
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
    print(solution.Print(root))

