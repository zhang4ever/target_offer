#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : StringPermutation.py
# @Time    : 2018-04-12 14:58
# @Author  : zhang bo
# @Note    : 字符串（数字）的排列组合
"""

class Solution:
    """
    要求：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有
        字符串abc,acb,bac,bca,cab和cba
    思路: 先选定一个字符，然后在递归排列剩下的字符串组合。
    """
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        l_ss = list(ss)
        l_ss.sort()
        res = []
        for i in range(len(ss)):
            if i > 0 and l_ss[i] == l_ss[i-1]:
                continue
            temps = self.Permutation(''.join(l_ss[:i]) + ''.join(l_ss[i+1:]))  # 递归出去i的其他组合
            for j in temps:
                res.append(l_ss[i]+j)
        return res
    """
    拓展：输入一个字符串,按字典序打印出该字符串中所有字符的排列。例如输入字符串abc,则打印出由字符a,b,c, ab, ac , bc, abc
    思路: 这种组合的长度可以是1,2,...,n.所以在长度为m的组合里面，先选定一个字符，如果该字符在组合中，那么再剩下的n-1里面选择m-1
    """
    def GroupAll(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        l_ss = list(ss)
        l_ss.sort()
        res = []
        for i in range(len(ss)):
            res.append(l_ss[i])
            if i > 0 and l_ss[i] == l_ss[i-1]:
                continue
            temps = self.GroupAll(''.join(l_ss[i+1:]))
            for j in temps:
                res.append(l_ss[i]+j)
                res = list(set(res))
                res.sort()
        return res
    
    """
        相关题目：输入含有八个数字的数组，判断有没有可能吧这八个数字分诶放置在正方体的八个定点上没事的三组向对面的四个定点的盒都相等
        思路：先对这八个数字进行排列组合；然后判断是否满足条件
    """
    def is_equal(self, array):
        is_find = False
        if not array or len(array) < 8:
            is_find = False
        # 排列组合这个数组
        res = self.group_array(array)
        for a in res:
            if a[0] + a[1] + a[2] + a[3] == a[4] + a[5] + a[6] + a[7] and \
               a[0] + a[2] + a[4] + a[6] == a[1] + a[3] + a[5] + a[7] and \
               a[0] + a[1] + a[4] + a[5] == a[2] + a[3] + a[6] + a[7]:
                print('找到组合:%s, 和是：%s' % (a, sum(a)/2))
                is_find = True
                break
        return is_find

    # 对一个数组进行全排列
    def group_array(self, array):
        if not array:
            return
        if len(array) == 1:
            return [array]
        res = []
        for i in range(len(array)):
            if i > 0 and array[i] == array[i - 1]:
                continue
            temps = self.group_array(array[0:i] + array[i+1:])
            for j in temps:
                res.append([array[i]]+j)
        return res

    """
    相关题目：N后问题。在8x8的国际象棋中摆放8个皇后，要求之间不能相互攻击，即：任意两个不同行/不同列/不同对角线。共有多少种摆放方法
    思路：由于不同行和不同列，那么每行只有一个，每列只有一个。那么可以只用0-7来初始化一个数组，标识第i行的那个皇后的列号。全排列后，
        然后判断是否满足对角线要求即可
    """
    def N_queen(self, columns):
        res = self.group_array(columns)  # 全排列
        count = 0
        for column in res:
            check = True  # 判断是否满足条件
            for i in range(len(column)):
                for j in range(i + 1, len(column)):
                    if i - j == column[i] - column[j] or i - j == column[j] - column[i]:
                        check = False
            if check:  # 满足条件
                count += 1
        print(len(res))
        return count


if __name__ == '__main__':
    ss = 'aabc'  # 按照字典顺序
    ss1 = 'acba'  # 不安
    ss2 = ''
    ss3 = 'abc'
    solution = Solution()
    print(solution.Permutation(ss))
    print(solution.Permutation(ss1))
    print(solution.GroupAll(ss1))
    ss4 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(solution.group_array(ss4))
    print(solution.is_equal(ss4))
    
    columns = [x for x in range(8)]  # N后问题
    print(solution.N_queen(columns))


