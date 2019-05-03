# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 0018 22:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0032_longestValidParentheses.py
# @Software: PyCharm

'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

import queue
class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        if s == "":
            return 0
        N = len(s)
        dp = [0 for i in range(N + 1)]
        res = 0
        for i in range(2, N + 1):
            if s[i - 1] == ')':
                if s[i - 2] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 2] == ')' and i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 2] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                res = max(res, dp[i])
        return res


    def longestValidParentheses_1(self, s: 'str') -> 'int':
        if s == "":
            return 0
        stack1 = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(i)
            else:
                stack1.pop()
                if stack1 == []:
                    stack1.append(i)
                else:
                    res = max(res, i - stack1[len(stack1) - 1])
        return res

    def longestValidParentheses_2(self, s: 'str') -> 'int':
        if s == "":
            return 0
        res = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2*right)
            elif left < right:
                left = right = 0

        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0
        return res

if __name__ == "__main__":
    a = Solution()
    s = ")()())"
    res = a.longestValidParentheses(s)
    print(res)
    res = a.longestValidParentheses_1(s)
    print(res)
    res = a.longestValidParentheses_2(s)
    print(res)