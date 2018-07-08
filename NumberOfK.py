#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NumberOfK.py
# @Time    : 2018-07-08 16:55
# @Author  : zhang bo
# @Note    : 数字在排序数组中出现的次数
"""

'''
题目描述：统计一个数字在一个排序数组中出现的次数。
示例：输入{1,2,3,3,3,3,4,5}和数字3，则3在数组中出现了4次
思路1：顺序遍历，时间复杂度是O(n),不高效
思路2：由于是排序好的数组，所有使用二分查找的方法。先使用二分法找到第一个出现的k，然后找到最后一个k,这样就可以确定k在数组中出现的次数。(logn)
'''
class Solution:
    # 使用二分查找统计。时间复杂度O(logN)
    def GetNumberOfK(self, data, k):
        """
        :return: 不存在或者异常返回0；否则返回次数
        """
        if not data or len(data) == 0:
            return 0
        start = 0
        end = len(data) - 1
        first = self.GetFirstK(data, k, start, end)
        last = self.GetLastK(data, k, start, end)
        if first > -1 and last > -1:
            return last - first + 1
        return 0

    # 使用二叉查找找到第一个k
    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        mid_data = data[mid]
        if mid_data == k:
            # 关键代码
            if mid > 0 and data[mid - 1] != k or mid == 0:  # 前面没有，说明当前刚好是第一个
                return mid
            else:  # 前面还有，继续找
                end = mid - 1
        elif mid_data > k:
            end = mid - 1
        else:
            start += 1
        return self.GetFirstK(data, k, start, end)

    # 使用二分查找找到最后一个k
    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        mid_data = data[mid]
        if mid_data == k:
            if (mid < end and data[mid + 1] != k) or mid == end:  # 后面没了，说明当前就是最后一个
                return mid
            else:  # 后面还有，继续找
                start = mid + 1
        elif mid_data > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.GetLastK(data, k, start, end)


if __name__ == '__main__':
    solution = Solution()
    data1 = [1, 2, 3, 3, 3, 3, 4, 5]
    data2 = []
    k = 6
    print(solution.GetNumberOfK(data1, k))
    print(solution.GetNumberOfK(data2, k))
