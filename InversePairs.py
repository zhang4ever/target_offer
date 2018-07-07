#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : InversePairs.py
# @Time    : 2018-07-06 19:14
# @Author  : zhang bo
# @Note    : 数组中的逆序对
"""

'''
题目描述：在数组中的两个数字如果前面一个特数字大于后面的数字。则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数
示例：数组{7，5，6，4},一共有5个逆序对，(7,6), (7,5),(7,4),(5,4), (6,4)
思路1:常规的两次遍历。时间复杂度O(n2)
思路2:归并。先将数组分割成子数组。先统计出没饿过子数组内部的逆序对；在统计两个相邻的子数组之间的逆序对。在统计的时候需要排序。O(nlogn)
备注：python的版本在牛客的测试上通不过，原因是时超时。
'''

class Solution:
    # 解法1：最原始的方法,顺序遍历O(n2)
    def InversePairs(self, data):
        # res = []
        ans = 0
        for i in range(len(data)):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    # res.append((data[i], data[j]))
                    ans += 1
        # print(res)
        return ans

    # 使用归并排序的方法，时间复杂度O(nlogn)
    def InversePairs2(self, data):
        if not data or len(data) == 0:
            return 0
        copy = [0]*len(data)  # 辅助数组
        for i in range(len(data)):
            copy[i] = data[i]
        count = self.GetInversePairs(data, copy, 0, len(data)-1)
        return count % 1000000007

    def GetInversePairs(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start)//2  # 将数组划分成两半
        # 1.递归左子数组
        left_count = self.GetInversePairs(data, copy, start, start+length)
        # 2.递归右子数组
        right_count = self.GetInversePairs(data, copy, start+length+1, end)
        # 3.统计左右两个子数组之间的逆序对数
        i = start + length  # 前半段的末尾
        j = end  # 后半段的末尾
        count = 0  # 统计逆序对的个数
        copy_index = end  # 逆向向辅助数组里面添加
        while i >= start and j >= start+length+1:  # i, j 两个指针分别向前移动，直到其中一个指向start位置
            if data[i] > data[j]:
                copy[copy_index] = data[i]
                copy_index -= 1
                i -= 1
                count += j - start - length
            else:
                copy[copy_index] = data[j]
                copy_index -= 1
                j -= 1

        # 如果i,j 其中一个回到start的位置时，另外一个还没有回到start
        while i >= start:  # 逆序i
            copy[copy_index] = data[i]
            copy_index -= 1
            i -= 1
        while j >= start+length+1:
            copy[copy_index] = data[j]
            copy_index -= 1
            j -= 1
        # print(copy)
        for i in range(start, end+1):
            data[i] = copy[i]
        return left_count + right_count + count

    # 使用Python内置的方法进行
    def InversePairs3(self, data):
        copy = data[:]
        copy.sort()
        count = 0
        i = 0
        while i < len(copy):
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    data1 = [7, 5, 6, 4]
    data2 = [1, 2, 3, 4, 5, 6, 7, 0,6]
    print(solution.InversePairs2(data2))
    # print(solution.InversePairs3(data2))