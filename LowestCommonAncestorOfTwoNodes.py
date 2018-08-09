#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : LowestCommonAncestorOfTwoNodes.py
# @Time    : 2018-08-09 15:49
# @Author  : zhang bo
# @Note    : 树节点的最低公共祖先
"""

"""
描述：给定两个节点，查找这两个节点的最低公共祖先
思路1：如果这个树是二叉搜索树：如果这两个节点比root小，那就在root的左子树中继续寻找；如果这两个节点比root大，那就在root的右子树中继续寻找；
思路2：如果这个树不是二叉搜索树，但是每个节点都有一个指向其父节点的指针，那么此问题就可以转化成求两个链表的第一个公共节点
思路3：如果树是普通的树，而且树中没有从节点指向父节点的指针
"""
# 二叉搜索树
class TreeNode1:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 非搜索树，但是有指向父节点指针
class TreeNode2:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    # 1. 假如树是二叉搜索数
    def query1(self, head, node1, node2):
        if not head or not node1 or not node2:
            return
        val1, val2 = node1.val, node2.val
        while head:
            if head.val > max(val1, val2):  # 在左子树中找
                head = head.left
            elif head.val < min(val1, val2):
                head = head.right
            else:
                return head

    # 2. 假如树不是二叉搜索树，但是每个节点都有一个指向父节点的指针
    def query2(self, head, node1, node2):
        if not head or not node1 or not node2:
            return
        len1 = self.getLengtFromNodeToRoot(node1)
        len2 = self.getLengtFromNodeToRoot(node2)
        long, short = (node1, node2) if len1 >= len2 else (node2, node1)
        for i in range(abs(len1-len2)):
            long = long.parent
        while short and long and long != short:
            long = long.parent
            short = short.parent
        return long

    # 3. 如果不是二叉搜素树，也没有指向父节点的指针
    def query3(self, head, node1, node2):
        if not head or head == node1 or head == node2:
            return head
        ltree = self.query3(head.left, node1, node2)
        rtree = self.query3(head.right, node1, node2)
        if ltree and rtree:
            return head
        return ltree if ltree else rtree


    # 获取一个节点到根结点的长度
    def getLengtFromNodeToRoot(self, node):
        if not node:
            return 0
        length = 0
        pNode = node
        while pNode:
            pNode = pNode.parent
            length += 1
        return length


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = TreeNode1(5), TreeNode1(2), TreeNode1(7)
    node4, node5, node6 = TreeNode1(1), TreeNode1(3), TreeNode1(4)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node5.right = node6
    tree1 = node1
    node1, node2, node3 = TreeNode2(1), TreeNode2(2), TreeNode2(3)
    node4, node5, node6 = TreeNode2(4), TreeNode2(5), TreeNode2(6)
    node1.left, node1.right = node2, node3
    node2.left, node2.right, node2.parent = node4, node5, node1
    node3.parent, node4.parent = node1, node2
    node5.left, node5.parent = node6, node2
    node6.parent = node5
    tree2 = node1
    # print(solution.query1(tree1, node5, node6).val)
    print(solution.query2(tree2, node4, node6).val)
    node1, node2, node3 = TreeNode1(1), TreeNode1(4), TreeNode1(6)
    node4, node5, node6 = TreeNode1(2), TreeNode1(1), TreeNode1(7)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node5.right = node6
    tree3 = node1
    print(solution.query3(tree3, node1, node5).val)