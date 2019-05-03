# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 19:28
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0022_generateParenthesis.py
# @Software: PyCharm

'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n: 'int') -> 'list[str]':
        # 回溯法
        res = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack()
        return res

    def generateParenthesis_1(self, n: 'int') -> 'list[str]':
        '''
        p is the parenthesis-string built so far,
        left and right tell the number of left and right parentheses still to add,
        and parens collects the parentheses.
        '''
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens.append(p)
            return parens

        return generate('', n, n)

    def generateParenthesis_2(self, n: 'int') -> 'list[str]':
        memo = {0: {''}}
        def dp(k):
            if k not in memo:
                memo[k] = {l + r for i in range(1, k) for l in dp(i) for r in dp(k - i)}
                memo[k] |= {'(' + c + ')' for c in dp(k - 1)}
            return memo[k]

        return list(dp(n))

if __name__ == "__main__":
    a = Solution()
    n = 3
    print(a.generateParenthesis(n))
    print(a.generateParenthesis_1(n))
    print(a.generateParenthesis_2(n))
