#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PrintTreesInLines.py
# @Time    : 2018-07-18 22:26
# @Author  : zhang bo
# @Note    : 从上到下分行打印二叉树
"""

'''
题目描述：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
思路：还是使用队列。设置两个指标toBePrint和nextLevel ，来记录当前层和下一层的节点的个数。先将头节点加入队列，每次出队时都输出，
        toBePrint-1 .之后将左右孩子加入队列，nextLevel+1.如果toBePrint == 0：换行。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]  # 现将头入列
        res = []  # 二维数组
        curr_res = []
        toBePrint = 1  # 要打印的层上的节点个数
        nextLevel = 0  # 下一层要打印的节点的个数
        while queue:

            current = queue.pop()  # 出队
            print(current.val, end=' ')
            curr_res.append(current.val)
            toBePrint -= 1
            if current.left:  # 将左孩子入队
                queue.insert(0, current.left)
                nextLevel += 1
            if current.right:  # 将右孩子入队
                queue.insert(0, current.right)
                nextLevel += 1

            if toBePrint == 0:
                print('', end='\n')  # 当前层的已经打完，换行
                res.append(curr_res)
                toBePrint = nextLevel  # 到下一层
                nextLevel = 0  # 每到一层，都要重新统计该层的节点的个数
                curr_res = []
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