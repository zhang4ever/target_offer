#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : DuplicateInArray.py
# @Time    : 2018-07-13 19:21
# @Author  : zhang bo
# @Note    : 数组中重复的数字
"""
'''
题目描述：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
        也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
示例：如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
思路1：使用栈。先对数组进行排序，然后入栈。栈顶的数字要是和即将入栈的数字一样，则返回该值时间复杂度和空间复杂度O(n)
思路2：更高效的方法。利用条件所有的值都位于(0, n-1)区间；那么如果numbers[i] == numbers[numbers[i]]则返回该值，否则交换；
'''
class Solution:

    # 使用栈
    def duplicate(self, numbers, duplication):
        if not numbers or len(numbers) ==0:
            return False
        numbers.sort()
        res_satck = []
        for i in numbers:
            if res_satck and i == res_satck[-1]:
                duplication[0] = i
                return True
            else:
                res_satck.append(i)
        return False

    # 更高效的办法
    def duplicate2(self, numbers, duplication):
        if not numbers or len(numbers) == 0:  # None或者[]
            return False
        for i in numbers:  # numbers不合法
            if i < 0 or i > len(numbers):
                return False
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    print(numbers[i])
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]  # 交换
        return False


if __name__ == '__main__':
    solution = Solution()
    numbers1 = [2, 3, 1, 0, 2, 5, 3]
    numbers2 = [2, 1, 3, 1, 4]
    duplication = [0]
    print(solution.duplicate(numbers2, duplication))
    print(solution.duplicate2(numbers1, duplication))