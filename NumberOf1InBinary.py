#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NumberOf1InBinary.py
# @Time    : 2018-03-29 14:59
# @Author  : zhang bo
# @Note    : 二进制表示中1的个数
"""

'''
题目描述：请实现一个函数， 输出该数二进制表示中1的个数。例如把9转化成二进制1001， 有2位是1，因此输入9， 返回2
思路：设置flag=1,对于输入的整数n, 依次和flag做与运算，，就可以判断n的依次低位是不是1，如果最低位的为1， 则1的个数+1；
    循环直到flag=0
'''
import time

class Solution:

    def NumberOf1(self, n):
        flag = 1
        count = 0
        if n < 0:
            n = n & 0xffffffff
        for i in range(int.bit_length(n)):  # 循环整数的二进制的所有位数
            if n & flag:  # 低位、次低位、、、
                count += 1
            flag = flag << 1  # 左移
        return count

    # 一个整数n-1再与n做&, 会将一个数的二进制表示的最右边一个1编程0；那么一个整数可以做多少次这样的运算，就说明有多少个1
    def NumberOf2(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count

    # 使用python内置函数bin()
    def NumberOf3(self, n):
        s = bin(n & 0xffffffff) if n < 0 else bin(n)
        return s.count('1')

    def run_time(self, func, n):
        s1 = time.clock()
        res1 = func(n)
        e1 = time.clock()
        print('func: %s, result:%s, time: %s' % (func.__name__, res1, (e1-s1)))

    '''
    题目拓展：请实现一个函数， 判断一个数是不是2的整数次方
    思路：一个数是2的整数次方，说明该数的二进制中只有一个1
    '''
    def NumberOf4(self, n):
        boo = True if (n-1) & n == 0 else False
        return boo

    # 给定两个数m, n，问改变m的多少位才可以将m变成n
    def NumberOf5(self, m, n):
        xor = m ^ n
        # 然后计算该亦或的结果中有多少个1（^-^）
        return self.NumberOf2(xor)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    solution.run_time(solution.NumberOf1, n)
    solution.run_time(solution.NumberOf2, n)
    solution.run_time(solution.NumberOf3, n)
    print(solution.NumberOf4(n))
    print(solution.NumberOf5(3, 4))



