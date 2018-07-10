#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseWordsInSentences.py
# @Time    : 2018-07-10 09:57
# @Author  : zhang bo
# @Note    : 反转单词顺序
"""

'''
    题目描述：输入一个英文句子，翻转句子中的单词的顺序，但单词内部的字符顺序不变
    示例：输入“I am a student.”, 输出“student. a am I”
    思路：先将整个字符串的所有字符全部翻转；然后根据空格分割，对单个单词就行翻转。       
'''

class Solution:
    # 解法1：两次反转
    def ReverseSentence(self, s):
        if not s or len(s) == 0:
            return ''
        s_list = list(s)
        self.Reverse(s_list)  # 整体翻转
        start, end = 0, 0
        res = []  # 由于字符串不可改变，所以新建一个list来保存反转后的结果
        while end < len(s):
            if end == len(s) - 1:  # 句子末尾
                res.append(self.Reverse(s_list[start:]))
            if s_list[start] == ' ':
                res.append(' ')
                start += 1
                end += 1
            elif s_list[end] == ' ':
                res.append(self.Reverse(s_list[start: end]))  # 对单个单词进行反转
                start = end
            else:
                end += 1
        return self.JoinToSentence(res)

    # 解法2: 最简单的解法
    def ReverseSentence2(self, s):
        return ' '.join(s.split(' ')[::-1])

    # 解法3: 使用栈
    def ReverseSentence3(self, s):
        res = []  # 栈
        ans = ''
        s = s.split(' ')
        for i in s:  # 入栈
            res.append(i)
        while res:
            ans += res.pop()+' '
        del res
        return ans[:-1]

    # 将一个字符数组合并成句子
    def JoinToSentence(self, a_list):
        s = ''
        for i in a_list:
            s += ''.join(i)
        return s

    # 整体翻转
    def Reverse(self, s_list):
        if not s_list or len(s_list) == 0:
            return []
        start = 0
        end = len(s_list) - 1
        while start < end:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
        return s_list


if __name__ == '__main__':
    solution = Solution()
    s1 = 'I am a student.'
    s2 = ''
    print(solution.ReverseSentence(s1))
    print(solution.ReverseSentence2(s1))
    print(solution.ReverseSentence3(s1))
