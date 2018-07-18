#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RegularexpressionMatching.py
# @Time    : 2018-07-18 10:57
# @Author  : zhang bo
# @Note    : 正则表达式的匹配
"""

'''
题目描述：实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
思路：主要考虑pattern的第2位是不是*或者s和pattern的第1位是不是相同两种情况来讨论。
'''
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:  # ‘’匹配‘’
            return True
        return self.matchCore(s, pattern)

    def matchCore(self, s, pattern):

        if s == pattern:  # 完全相等，肯定匹配
            return True
        elif pattern == '':
            return False
        if s == '':
            if pattern == '.':
                return False
            elif len(pattern) == 1 or pattern[1] != '*':
                return False
            else:
                return self.matchCore(s, pattern[2:])
        # pattern的第二个是*，前面可以出现0个或则多个，所以pattern可以进入下一状态，也可保持当前状态，甚至跳过*
        if len(pattern) >= 2 and pattern[1] == '*':
            if s[0] == pattern[0] or pattern[0] == '.':  # 第一个匹配时
                return self.matchCore(s[1:], pattern[2:]) or self.matchCore(s[1:], pattern) or \
                       self.matchCore(s, pattern[2:])
            else:  # 第一个不匹配时，只能跳过pattern的*指望后面的
                return self.matchCore(s, pattern[2:])
        # pattern第二个不是*, 如果第一个相同，则匹配下一个， 否则False
        if s[0] == pattern[0] or pattern[0] == '.':
            return self.matchCore(s[1:], pattern[1:])
        return False


if __name__ == '__main__':
    solution = Solution()
    s = 'aaa'
    pattern = 'aaa*'
    print(solution.match(s, pattern))
