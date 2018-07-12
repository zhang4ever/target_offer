#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : DicesProbability.py
# @Time    : 2018-07-11 20:56
# @Author  : zhang bo
# @Note    : n个骰子的点数

"""

'''
题目描述：把n个骰子扔在地上，所有的骰子朝上一面的点数之和为s，输入n，打印出s的所有可能的值出现的概率。
思路1：使用递归的思想。可以将n个骰子分为两组，一组有1个，另一组n-1个；所有的和的可能结果是n到6n; 那么就可以将和s保存在数组的第s-n个位置，
      例如2个骰子时，array[0]=2， array[1]=3, array[s-n] = s; 
思路2：使用概率的知识。和为s的概率就是和为s的所有组合的概率之和，p(S)=sum(p(s)), p(s)表示每一种组合。而每一种和为s的组合的概率，为
      p(s)=p(sum(i))=sum(p(i)), p(i)就是每一个骰子出现点数为i的概率。通过建立两个数组来存放每种结果的次数，一个数组的第n项等于另一个
      数组的(n-1),(n-2)...(n-6)的和。不断地交换两个数组来重复实现。空间复杂度O(n) ,时间复杂度
      O(n*n*logn)
      
'''
g_max = 6  # 每个骰子的最大点数

class Solution:
    # 递归的思想
    def PrintProbability(self, number):
        if number < 1:
            return
        sum_max = g_max * number  # 最大的和是6n
        p_probabilities = [0] * (sum_max - number + 1)  # 所有可能出现的结果
        self.GetProbability(number, p_probabilities)  # 计算每种可能出现的概率
        total = pow(g_max, number)  # 所有可能的组合
        for i in range(number, sum_max + 1):  # 打印
            ratio = p_probabilities[i - number] / total
            print('sum:%s, ratio:%s' % (i, ratio))
        del p_probabilities

    # 基于循环
    def PrintProbability2(self, number):
        probabilities = [[0] * (g_max * number + 1), [0] * (g_max * number + 1)]  # 两个数组分别存储和为s的次数
        flag = 0
        for i in range(1, g_max + 1):  # 每个骰子每一面出现的概率都是1/6
            probabilities[flag][i] = 1.0
        for k in range(2, number+1):  # 剩下的每个骰子
            for i in range(k):  # 将不可能出现的和的结果为0；比如两个骰子时和的最小是2，所以0，1位置就是0
                probabilities[1-flag][i] = 0
            for i in range(k, g_max*k+1):  # 和为s的每种组合[n, 6n]
                probabilities[1-flag][i] = 0  # 初始化全置0
                j = 1
                while j <= i and j <= g_max:
                    probabilities[1-flag][i] += probabilities[flag][i-j]  # 更新每个可能的结果的次数，
                    j += 1
            flag = 1-flag
        total = pow(g_max, number)  # 所有可能的组合
        for i in range(number, g_max*number + 1):  # 打印
            print('sum:%s, ratio:%s' % (i, probabilities[flag][i] / total))

    # 计算每种可能出现的次数
    def GetProbability(self, number, probability):
        for i in range(1, g_max + 1):
            self.Probability(number, number, i, probability)

    # 递归
    def Probability(self, origin, current, curr_sum, probabilities):
        if current == 1:  # 只有1个骰子时，和为1到g_max
            probabilities[curr_sum - origin] += 1
        else:
            for i in range(1, g_max + 1):
                self.Probability(origin, current - 1, i + curr_sum, probabilities)


if __name__ == '__main__':
    solution = Solution()
    number = 2
    solution.PrintProbability(number)
    solution.PrintProbability2(number) 
