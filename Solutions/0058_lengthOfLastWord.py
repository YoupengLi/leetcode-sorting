# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 0015 07:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0058_lengthOfLastWord.py
# @Software: PyCharm

'''
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5

'''
class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        if not s or len(s) <= 0:
            return 0
        s = s.rstrip()
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] is " ":
                return count
            count += 1
        return count

    def lengthOfLastWord_1(self, s: 'str') -> 'int':
        if not s or len(s) == 0:
            return 0
        s = s.rstrip()
        words = s.split(' ')
        return len(words[-1])

if __name__ == "__main__":
    a = Solution()
    s = "Hello World"
    res = a.lengthOfLastWord(s)
    print(res)
    res = a.lengthOfLastWord_1(s)
    print(res)