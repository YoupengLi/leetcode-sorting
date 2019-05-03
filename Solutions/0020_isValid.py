# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 09:25
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0020_isValid.py
# @Software: PyCharm

'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if s == "":
            return True
        str = ["()", "[]", "{}"]
        while str[0] in s or str[1] in s or str[2] in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        if s == "":
            return True
        else:
            return False

    def isValid_1(self, s: 'str') -> 'bool':
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        par_map = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i not in par_map:
                stack.append(i)
            elif not stack or stack.pop() != par_map[i]:
                return False
        return not stack

    def isValid_2(self, s: 'str') -> 'bool':
        if len(s) % 2 == 1:
            return False
        v = []
        d = {']': '[', ')': '(', '}': '{'}
        for i in range(len(s)):
            if s[i] in d.values():
                v.append(s[i])
            elif s[i] in d.keys():
                if len(v) == 0:
                    return False
                elif v[-1] == d[s[i]]:
                    v.pop()
                else:
                    return False
        if v == []:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Solution()
    s = "{[]}"
    print(a.isValid(s))
    print(a.isValid_1(s))
    print(a.isValid_2(s))
    s = "([)]"
    print(a.isValid(s))
    print(a.isValid_1(s))
    print(a.isValid_2(s))