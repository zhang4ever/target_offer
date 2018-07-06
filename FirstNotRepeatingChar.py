#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : FirstNotRepeatingChar.py
# @Time    : 2018-07-05 22:29
# @Author  : zhang bo
# @Note    : 第一个只出现一次的字符
"""
'''
题目描述：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1.
示例：输入"abassdeff"，输出'b'
思路1：直接遍历字符串的每个元素，与后面的比较。但是这样遍历一次O(N),查找一次O(N)，所以时间复杂度O(n2)
思路2：使用hash的原理，将字符串映射到hash表(key-字符; val-次数)。在遍历一次字符串，返回第一个val为1的key。时间复杂度为O(n)
拓展：从第一个字符串中删除第二个字符串中已经出现过的字符。同样使用hash来存放第二个字符，这样只需要遍历第一个字符串就好，时间复杂度O(n).
'''
class Solution:
    # 解法1：直接遍历，时间复杂度O(n2)
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        res = [s.count(i) for i in s]
        return s[res.index(1)]

    # 使用hash的方式O(N)
    def FirstNotRepeatingChar2(self, s):
        if not s:
            return -1
        res_dict = {}
        s_set = set(list(s))
        for i in s_set:  # 初始化hash
            res_dict[i] = 0
        for j in s:  # 构造hash
            res_dict[j] += 1
        for k in s:
            if res_dict[k] == 1:
                return k

    # 题目拓展：判断两个单词是不是互变次（两个单词的字符一样，每个字符出现的次数也一样）
    def IfAnagram(self, s1, s2):
        """
        思路: 首先建立一个hash，存放第一个字符串；然后遍历第二个字符串，扫描到一个，val就-1；最后如果hash的所有的val都为1，则return T
        """
        if not s1 or not s2:
            return False
        res_dict = {}
        for i in s1:  # 构造hash
            if i not in res_dict.keys():
                res_dict[i] = 1
            else:
                res_dict[i] += 1
        for j in s2:  # 扫描s2
            if j not in res_dict.keys():
                return False
            else:
                res_dict[j] -= 1
        return set(res_dict.values()).pop() == 0


if __name__ == '__main__':
    solution = Solution()
    s1 = 'abassdeff'
    s2 = ''
    print(solution.FirstNotRepeatingChar2(s1))
    str1, str2 = 'silent', 'listen'
    str1, str2 = 'google', 'glooge'
    print(solution.IfAnagram(str1, str2))
