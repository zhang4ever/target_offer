#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseWordsInSentences.py
# @Time    : 2018-07-10 09:57
# @Author  : zhang bo
# @Note    : 反转单词顺序 VS 左旋转字符串
"""

class Solution:
    """
        题目描述：输入一个英文句子，翻转句子中的单词的顺序，但单词内部的字符顺序不变
        示例：输入“I am a student.”, 输出“student. a am I”
        思路；然后根据空格分割，对单个单词就行翻转。
    """
    # 解法1：两次反转
    def ReverseSentence(self, s):
        if not s or len(s) == 0:
            return ''
        s_list = list(s)
        self.Reverse(s_list)  # 整体翻转
        start, end = 0,
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


class Solution2:
    """
        题目描述：字符串的左旋转操是指将字符串的前面若干个字符转移到字符串的尾部。
        示例：输入："abcdefg", 输出"cdefgab"
        思路：根据n将字符串分为两个部分，然后分别对两个字符串进行反转，再拼接；最后在对拼接后的在反转一次即可。
    """
    def LeftRoatateString(self, s, n):
        if not s or len(s) == 0 or len(s) < n or n <0:
            return ''
        s = list(s)
        s1 = solution.Reverse(s[:n])
        s2 = solution.Reverse(s[n:])
        print(s1)
        res = solution.Reverse(s1+s2)
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    s1 = 'I am a student.'
    s2 = ''
    s = 'abcdefg'
    print(solution.ReverseSentence(s1))
    print(solution.ReverseSentence2(s1))
    print(solution.ReverseSentence3(s1))

    solution2 = Solution2()
    s = 'abcdefg'
    n = 2
    print(solution2.LeftRoatateString(s, n))
