# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 10:02
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0151_reverseWords.py
# @Software: PyCharm

'''
151. Reverse Words in a String

Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However,
your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up:For C programmers, try to solve it in-place in O(1) extra space.
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

    def reverseWords_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s.reverse()
        return " ".join(s)

    def reverseWords_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        s = s.split()
        if len(s) == 1:
            return s[0]
        s.reverse()
        s = ' '.join(s)
        return s

if __name__  == "__main__":
    a = Solution()
    s = "the sky is blue"
    print(a.reverseWords(s))
    print(a.reverseWords_1(s))
    print(a.reverseWords_2(s))
    s = "  hello world!  "
    print(a.reverseWords(s))
    print(a.reverseWords_1(s))
    print(a.reverseWords_2(s))
    s = "a good   example"
    print(a.reverseWords(s))
    print(a.reverseWords_1(s))
    print(a.reverseWords_2(s))