#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : StringPathInMatrix.py
# @Time    : 2018-07-17 14:29
# @Author  : zhang bo
# @Note    : 矩阵中的路径
"""

'''
题目描述：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
示例：例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
        因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
思路：使用回溯法。首先建立一个数组来保存每个方块是否别访问过的状态；遍历矩阵中的每个元素，判断当前的元素是否被访问过，如果没有，继续
    在该元素周围递归是否存在路径。
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or len(matrix) == 0 or rows < 1 or cols < 1 or len(path) == 0:
            return
        visited = [False] * len(matrix)
        path_length = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, path, row, col, visited, path_length):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, path, row, col, visited, path_length):

        if path_length == len(path):
            return True
        hasPath = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[path_length] \
                and visited[row * cols + col] is False:
            path_length += 1
            visited[row * cols + col] = True
            # 判断是否有路径
            hasPath = self.hasPathCore(matrix, rows, cols, path, row - 1, col, visited, path_length) or \
                      self.hasPathCore(matrix, rows, cols, path, row, col-1, visited, path_length) or \
                      self.hasPathCore(matrix, rows, cols, path, row, col + 1, visited, path_length) or \
                      self.hasPathCore(matrix, rows, cols, path, row+1, col, visited, path_length)
            if not hasPath:
                path_length -= 1  # 回溯
                visited[row * cols + col] = False
        return hasPath


if __name__ == '__main__':
    solution = Solution()
    matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']
    rows, cols = 3, 4
    path = 'abcec'
    print(solution.hasPath(matrix, rows, cols, path))
