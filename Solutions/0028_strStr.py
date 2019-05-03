# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 0017 18:57
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0028_strStr.py
# @Software: PyCharm

'''
28. Implement strStr()

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if not needle:
            return 0
        if not haystack or needle not in haystack:
            return -1
        needle = list(needle)
        haystack = list(haystack)
        n_len = len(needle)
        h_len = len(haystack)
        if n_len > h_len:
            return -1
        else:
            for i in range(h_len - n_len + 1):
                if haystack[i] == needle[0]:
                    res = True
                    k = i
                    for j in range(1, n_len):
                        k += 1
                        if haystack[k] == needle[j]:
                            continue
                        else:
                            res = False
                            break
                    if res:
                        return i
                else:
                    continue
            return -1

    def strStr_1(self, haystack: 'str', needle: 'str') -> 'int':
        index = 0
        if len(needle) == 0:
            return 0

        if len(haystack) == 0 or needle not in haystack:
            return -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                if len(needle) > 0:
                    if haystack[index:index + len(needle)] == needle:
                        return index
                    index += 1
                else:
                    return -1

if __name__ == "__main__":
    a = Solution()
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    res = a.strStr(haystack, needle)
    print(res)
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    res = a.strStr_1(haystack, needle)
    print(res)