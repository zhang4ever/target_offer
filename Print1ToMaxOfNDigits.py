#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : Print1ToMaxOfNDigits.py
# @Time    : 2018-03-30 11:15
# @Author  : zhang bo
# @Note    : 
"""
import time

class Solution:
    """
    题目描述：输入数字n，按顺序打印从1到最大的n位十进制数。例如输入3， 打印1、2、3一直到最大的三位数即999
    思路：考虑大数问题，需将每个数按位分开，循环一次，新建一个数组保存一次，在打印一次，打印玩后立即删除（释放内存）
    """
    def pirnt1ToMaxOfDigits1(self, n):
        # write code here
        if n <= 0:
            return None
        number = ['0'] * n  # 初始化
        while not increment(number):
            printNumber(number)
        del number

    # 使用递归的思路
    def pirnt1ToMaxOfDigits2(self, n):
        if n <= 0:
            return None
        number = ['0'] * n  # init
        for i in range(10):
            number[0] = str(i)
            print1ToMaxOfDigitsRecursively(number, 0)
        del number

# 模拟加法运算
def increment(number):
    """
    判断一个数+1的时候，是否在最高位会产生进位，如果True, 说明已经达到看了最大值
    :number:相当于每调用increment()一次，number就会改变一次，+1
    :return: 如果最高位产生进位，return true,否则 return false
    """
    is_overflow = False  #
    n_takeover = 0
    n_len = len(number)
    i = n_len - 1
    while i >= 0:  # while-loop start
        n_sum = int(number[i]) + n_takeover
        if i == n_len - 1:  #
            n_sum += 1
        if n_sum >= 10:  # 满10
            if i == 0:  # 最高位>10, 表表示达到最大
                is_overflow = True
            else:
                n_sum -= 10  # 进位后清零
                n_takeover = 1  # 进1
                number[i] = str(n_sum)
        else:  # 不满10
            number[i] = str(n_sum)
            break
        # print(number)
        i -= 1  # while-loop end
    return is_overflow

# 打位印字符串
def printNumber(number):
    is_start_0 = True  # 第一位是否为0
    n_len = len(number)
    for i in range(n_len):  # for-loop start
        if is_start_0 and number[i] != '0':  # 之前在数字不够n位时，前面补了0，打印时，没必要打印出前面的0
            is_start_0 = False
        if not is_start_0:
            print('%s' % number[i], end='')
    print('')

# 递归打印
def print1ToMaxOfDigitsRecursively(number, index):
    if index == len(number) - 1:  # 最后位
        printNumber(number)
        return
    for i in range(10):
        number[index+1] = str(i)
        print1ToMaxOfDigitsRecursively(number, index+1)

def run_time(func, n):
    s1 = time.clock()
    res1 = func(n)
    e1 = time.clock()
    print('func: %s, result:%s, time: %s' % (func.__name__, res1, (e1-s1)))


if __name__ == '__main__':
    solution = Solution()
    n = 2
    run_time(solution.pirnt1ToMaxOfDigits1, n)
    run_time(solution.pirnt1ToMaxOfDigits2, n)
