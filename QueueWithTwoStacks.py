#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : QueueWithTwoStacks.py
# @Time    : 2018-03-25 19:51
# @Author  : zhang bo
# @Note    : 
"""
'''
问题描述：使用两个栈实现一个队列。实现两个函数push和pop,分别完成在队列的
          尾部插入节点和在队列头删除节点的功能。
          
思路：使用两个栈：stack1和stack2, 用stack1进行插入操作，然后将stack1的原色出栈， 
      压入stack2中，再从stack2删除
'''

## *********************使用两个栈实现队列*********************
class Solution:
    # 在队列的尾部插入节点
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    # 在队列的头部删除节点
    def pop(self):
        # 首先将stack1中的元素转移到stack2中
        if len(self.stack2) <= 0:  # stack2中空
            while len(self.stack1) > 0:  # stack1中有元素
                data = self.stack1.pop()
                self.stack2.append(data)
        # 从stack2中进行删除
        if len(self.stack2) == 0:
            print('队列为空，无法删除元素！')
            return None
        head = self.stack2.pop()
        return head


## ******************使用两个队列来实现栈*************************
class Solution2:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.insert(0, node)

    def pop(self):
        # 先将queue1中的元素转移到queue2中
        if len(self.queue2) <= 0:
            while len(self.queue1) > 0:
                data = self.queue1.pop()
                self.queue2.append(data)
        # 从queue2中删除
        if len(self.queue2) == 0:
            print('栈为空，无法完成出栈！')
            return None
        head = self.queue2.pop()
        return head


if __name__ == '__main__':
    solution = Solution()  # 测试两个栈实现队列
    solution.push(1)
    solution.push(2)
    solution.push(3)
    print(solution.stack1)
    print(solution.pop())
    print(solution.pop())

    solution2 = Solution2()  # 测试两个队列实现栈
    solution2.push(4)
    solution2.push(5)
    solution2.push(6)
    print(solution2.queue1)
    print(solution2.pop())
    print(solution2.pop())
