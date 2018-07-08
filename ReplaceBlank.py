#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReplaceBlank.py
# @Time    : 2018-03-23 16:08
# @Author  : zhang bo
# @Note    : 替字符串中的空格
"""
'''
描述：请实现一个函数，把字符串中的每个空格替换成“%20”， 例如输入 “We are happy.”，则输出“We%20are%20happy.”
要求：时间字符移动的次数为O(n)
'''
'''
思路：先统计出原始字符串的长度和替换后的长度。从尾部开始遍历，设置两个指针，一个指向原始串的末尾，一个指向替换后的末尾；
第一个指针向前遍历，依次复制字符串的内容，。直至第一个指针遇见空格，将其换成‘%20’
'''

class Solution:

    # s 源字符串
    def replaceSpace(self, s):

        if not isinstance(s, str) or len(s) == 0 or s is None:
            return ''
        # 首先计算原始串的长度和空格的数量
        origin_length = len(s)
        num_space = 0
        for i in s:
            if i == ' ':
                num_space += 1
        new_length = origin_length + 2 * num_space  # 替换后的长度

        # 设置两个指针
        index_origin = origin_length - 1
        index_new = new_length - 1
        new_s = new_length * [None]   # 新建一个空字符串

        while index_new > index_origin >= 0:
            if s[index_origin] == ' ':
                new_s[index_new - 2:index_new+1] = ['%', '2', '0']
                index_new -= 3
                index_origin -= 1
            else:  # 将前前面的指针扫过的字符复制到新的串中
                new_s[index_new] = s[index_origin]
                index_new -= 1
                index_origin -= 1
        # 将不需要移动的部分元素进行复制
        new_s[0: index_origin+1] = s[0: index_origin+1]
        return ''.join(new_s)


if __name__ == '__main__':
    s = 'We are happy.'
    s1 = ''
    s2 = 'hello world'
    s3 = 123
    solution = Solution()
    print(s)
    print(solution.replaceSpace(s))
