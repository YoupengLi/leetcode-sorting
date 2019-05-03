# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 09:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0017_letterCombinations.py
# @Software: PyCharm

'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    def letterCombinations(self, digits: 'str') -> 'list[str]':
        if not digits:
            return []
        dict1 = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = dict1[digits[0]]
        for i in digits[1:]:
            temp = []
            for j in dict1[i]:
                for k in res:
                    temp.append(k+j)
            res = temp
        return res

    def letterCombinations_1(self, digits: 'str') -> 'list[str]':
        mapping = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        return self.letterCombinationsHelper(digits, mapping, "", [])

    def letterCombinationsHelper(self, digits: 'str', mappings: 'dict', char: 'char', res: 'list[str]') -> 'list[str]':
        if len(digits) > 0:
            for newChar in mappings[digits[0]]:
                self.letterCombinationsHelper(digits[1:], mappings, char + newChar, res)
        else:
            if len(char) > 0:
                res.append(char)
        return res

if __name__ == "__main__":
    a = Solution()
    digits = "23"
    print(a.letterCombinations(digits))
    print(a.letterCombinations_1(digits))