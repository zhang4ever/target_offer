#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : GreatestSumOfSubarrays.py
# @Time    : 2018-07-04 16:52
# @Author  : zhang bo
# @Note    : 连续子数组的最大和
"""
'''
题目描述：输入一个整形数组，数组里面有整数和负数/数组中一个或者连续多个整数形成一个子数组。求所有子数组的和的最大值。时间复杂度O(N)
实例：输入数组{1，-2，3，10，-4，7，2，-5}， 输出和最大的子数组为{3，10，-4，7，2}， 和为18
思路1：直接枚举的时间复杂度为O(n2)
思路2：从第一个数子开始遍历，一依次加后面的数，如果发现结果比上一轮的有所减小，则记录当年的结果，并舍弃之前的数字，从当前的位置继续向后遍历；
      不断地比较新的结果并更新结果，最终返回和最大的结果
思路3：动态规划。当i=0或者f(i-1)<=0时f(i)=array[i]; 当i!=0 并且f(i-1)>0时，f(i)=f(i-1)+array[i]
'''


class Solution:
    # 解法1：累加，局部比较O(n)
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 0 or array is None:
            return
        curr_sum = 0  # 记录当前的和
        greatest_sum = array[0]
        res = []
        for data in array:
            if curr_sum <= 0:
                curr_sum = data
                res = [data]
            else:
                curr_sum += data
                res.append(data)
            if greatest_sum < curr_sum:
                greatest_sum = curr_sum
        print(res)
        return greatest_sum

    # 解法2：使用动态规划
    def FindGreatestSumOfSubArray2(self, array):
        if len(array) <= 0 or array is None:
            return
        ans = [0]*len(array)  # 返回结果
        for i in range(len(array)):
            if i == 0 or ans[i-1] <= 0:
                ans[i] = array[i]
            if i != 0 and ans[i-1] > 0:
                ans[i] = ans[i-1] + array[i]
        return max(ans)


solution = Solution()
array = [1, -2, 3, 10, -4, 7, 2, -5]
array1 = []
array2 = [1, -2, 3, 10, -4, 7, 2, 0]
array3 = [1]
print(solution.FindGreatestSumOfSubArray(array))
print(solution.FindGreatestSumOfSubArray2(array))
