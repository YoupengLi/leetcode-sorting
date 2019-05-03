# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 0008 07:42
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0014_longestCommonPrefix.py
# @Software: PyCharm

'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: 'list[str]') -> 'str':
        if not strs:
            return ""

        res = ""
        if len(strs) == 1:
            return strs[0]
        else:
            short = len(min(strs, key=len))
            q = 0
            flag = False
            while q < short:
                for i in range(len(strs)):
                    if i == 0:
                        a = strs[i][q]
                    else:
                        if a != strs[i][q]:
                            flag = True
                            break
                        elif i == len(strs)-1 and a == strs[i][q]:
                            res = res + a
                        else:
                            continue
                if flag:
                    return res
                q += 1

            return res

    def longestCommonPrefix_1(self, strs: 'list[str]') -> 'str':
        prefix = ""
        if not strs:
            return prefix
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for ch1, ch2 in zip(first, last):
            if ch1 == ch2:
                prefix += ch1
            else:
                break
        return prefix

    def longestCommonPrefix_2(self, strs: 'list[str]') -> 'str':
        if not strs:
            return ""
        # since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]  # stop until hit the split index
        return s1

if __name__ == "__main__":
    a = Solution()
    strs = ["flower", "flow", "flight"]
    print(a.longestCommonPrefix(strs))
    print(a.longestCommonPrefix_1(strs))
    print(a.longestCommonPrefix_2(strs))
    strs = ["dog", "racecar", "car"]
    print(a.longestCommonPrefix(strs))
    print(a.longestCommonPrefix_1(strs))
    print(a.longestCommonPrefix_2(strs))
