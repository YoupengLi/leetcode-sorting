# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:00
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0150_evalRPN.py
# @Software: PyCharm

'''
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result
and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
import math


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                b, a = stack[-1], stack[-2]
                a = a * 1.0
                stack.pop()
                stack.pop()
                stack.append((int(eval('a' + i + 'b'))))
        return stack[-1]

    def evalRPN_1(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in "+-*/":
                temp = int(i)
                stack.append(temp)
            else:
                b, a = stack[-1], stack[-2]
                stack.pop()
                stack.pop()
                if i == '+':
                    a = a + b
                elif i == '-':
                    a = a - b
                elif i == '*':
                    a = a * b
                else:
                    a = int(a * 1.0 / b)
                stack.append(a)

        return stack[-1]

    def evalRPN_2(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(float(i))
            else:
                b, a = stack.pop(), stack.pop()
                if i == '+':
                    a = a + b
                elif i == '-':
                    a = a - b
                elif i == '*':
                    a = a * b
                elif i == '/':
                    a = a / b
                    a = math.floor(a) if a > 0 else math.ceil(a)
                stack.append(a)

        return int(stack[-1])

if __name__ == "__main__":
    a = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    print(a.evalRPN(tokens))
    print(a.evalRPN_1(tokens))
    print(a.evalRPN_2(tokens))
    tokens = ["4", "13", "5", "/", "+"]
    print(a.evalRPN(tokens))
    print(a.evalRPN_1(tokens))
    print(a.evalRPN_2(tokens))
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(a.evalRPN(tokens))
    print(a.evalRPN_1(tokens))
    print(a.evalRPN_2(tokens))