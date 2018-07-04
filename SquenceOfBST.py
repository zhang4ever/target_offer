#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SquenceOfBST.py
# @Time    : 2018-04-09 09:47
# @Author  : zhang bo
# @Note    : 后序遍历搜索二叉树
"""

class Solution:

    """
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
    """
    def VerifySquenceOfBSTByPostOrder(self, sequence):
        if not sequence:  # 空树
            return False
        root = sequence[-1]  # 最后一个节点为root
        if root >= max(sequence) or root <= min(sequence):
            return True
        index = 0
        # 确定左子树
        for i in range(len(sequence)-1):
            if sequence[i] > root:  # 左子树的所有元素都比root小
                index = i
                break
        # 确定右子树
        for i in range(index+1, len(sequence)-1):
            if sequence[i] < root:  # 右子树的所有元素都比root大
                return False
        # 判断左子树是不是搜索树
        left = True
        if index > 0:  # 有左子树的话
            left = self.VerifySquenceOfBSTByPostOrder(sequence[:index])
        # 判断左子树是不是搜索树
        right = True
        if index < len(sequence)-1:  # 如果有右子树
            right = self.VerifySquenceOfBSTByPostOrder(sequence[index: len(sequence)-1])
        return left and right

    
    """拓展：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。"""
    def VerifySquenceOfBSTByPreOrder(self, sequence):
        if len(sequence) == 0:
            return False
        root = sequence[0]  # root节点
        if root >= max(sequence) or root <= min(sequence):
            return True
        # 确定左子树和右子树
        index = 0
        for i in range(1, len(sequence)):
            if sequence[i] > root:
                index = i
                break
        for i in range(index+1, len(sequence)):
            if sequence[i] < root:
                return False
        # 分别判断左子树和右子树是否为搜索树
        left = True
        if index > 0:
            left = self.VerifySquenceOfBSTByPreOrder(sequence[1: index])
        right = True
        if index < len(sequence)-1:
            right = self.VerifySquenceOfBSTByPreOrder(sequence[index: len(sequence)])
        return left and right

    
if __name__ == '__main__':
    solution = Solution()
    sequence1 = [5, 7, 6, 9, 11, 10, 8]
    sequence2 = [7, 4, 6, 7]
    sequence3 = [1, 2, 3, 4]
    sequence4 = [7, 6, 5, 4]
    sequence5 = []
    print(solution.VerifySquenceOfBSTByPostOrder(sequence5))
    sequence6 = [5, 4, 3, 6, 7, 8]
    sequence7 = [5, 6, 8, 7]
    print(solution.VerifySquenceOfBSTByPreOrder(sequence7))
