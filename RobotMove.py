#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RobotMove.py
# @Time    : 2018-07-17 16:55
# @Author  : zhang bo
# @Note    : 机器人的运动范围
"""
'''
题目描述：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
        但是不能进入行坐标和列坐标的数位之和大于k的格子。请问该机器人能够达到多少个格子？
示例：例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
思路：回溯法。先从(0,0)开始试探。如果进入(0, 0)后， 判断能不能进入其上下左右四个相邻的位置，然后递归。
'''


class Solution:
    def movingCount(self, threshold, rows, cols):
        if rows < 1 or cols < 1 or threshold < 0:
            return 0
        visited = [False] * (rows * cols)
        count = self.movingCountCore(rows, cols, 0, 0, visited, threshold)
        return count

    def movingCountCore(self, rows, cols, row, col, visited, threshold):
        count = 0
        if self.check(rows, cols, row, col, visited, threshold):  # 如果能进入下一个(i, j)
            visited[row * cols + col] = True  # 已经走过
            # 进入后判断能不能进入当前位置的四个邻近的位置， 递归
            count = 1 + self.movingCountCore(rows, cols, row - 1, col, visited, threshold) \
                      + self.movingCountCore(rows, cols, row + 1, col, visited, threshold) \
                      + self.movingCountCore(rows, cols, row, col - 1, visited, threshold) \
                      + self.movingCountCore(rows, cols, row, col + 1, visited, threshold)
        return count

    # 是否满足进入要求
    def check(self, rows, cols, row, col, visited, threshold):
        # 是否越界， 是否已经访问过， 是否满足位数要求
        if 0 <= row < rows and 0 <= col < cols and not visited[row * cols + col] \
                and (self.checkBitsSum(row) + self.checkBitsSum(col)) <= threshold:
            return True
        return False

    # 位数之和<阈值
    def checkBitsSum(self, num):
        ans = 0
        while num > 0:
            ans += num % 10
            num /= 10
        return ans


if __name__ == '__main__':
    solution = Solution()
    rows, cols = 8, 8
    threshold = 7
    print(solution.movingCount(threshold, rows, cols))