#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MinNumberInRoatedArray.py
# @Time    : 2018-03-26 14:54
# @Author  : zhang bo
# @Note    : 
"""

'''
描述：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，
    输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的
    所有元素都大于0，若数组大小为0，请返回0。
思路：使用二分查找。设置两个指针left和right,如果二分的结果mid的值大于left的值，说明最小的值最mid的右面；反之在左面。
    不断地缩小区间，通过不断移动两个指针，如果最后两个指针位置相邻，那么mid的值就是最小值
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        mid = left
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:  # 相邻
                mid = right
                break
            mid = int((left + right) / 2)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            if rotateArray[mid] <= rotateArray[left]:
                right = mid
            # 特殊case，存在多个元素相等，例如{1, 0, 1, 1, 1},此时直接顺序查找
            if rotateArray[left] == rotateArray[right] == rotateArray[mid]:
                return self.finMinByOrder(rotateArray, left, right)
        return rotateArray[mid]

    def finMinByOrder(self, array, left, right):
        result = array[left]
        for i in array:
            if result > i:
                result = i
        return result

if __name__ == '__main__':
    solution = Solution()
    rotateArray = [3, 4, 5, 1, 2]
    rotateArray1 = [1, 0, 1, 1, 1]
    rotateArray2 = [1, 1, 1, 0, 1]

    print(solution.minNumberInRotateArray(rotateArray1))