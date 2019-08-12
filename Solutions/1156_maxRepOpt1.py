# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 11:16
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1156_maxRepOpt1.py
# @Software: PyCharm

'''
1156. Swap For Longest Repeated Character Substring

Given a string text, we are allowed to swap two of the characters in the string.
Find the length of the longest substring with repeated characters.

Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then,
the longest repeated character substring is "aaa", which its length is 3.

Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated
character substring "aaaaaa", which its length is 6.

Example 3:
Input: text = "aaabbaaa"
Output: 4

Example 4:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

Example 5:
Input: text = "abcdef"
Output: 1

Constraints:
1 <= text.length <= 20000
text consist of lowercase English characters only.
'''

import itertools
from collections import Counter

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        count = Counter(text)
        res = max(min(k + 1, count[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res

if __name__ == "__main__":
    a = Solution()
    text = "ababa"
    print(a.maxRepOpt1(text))
    text = "aaabaaa"
    print(a.maxRepOpt1(text))
    text = "aaabbaaa"
    print(a.maxRepOpt1(text))
    text = "aaaaa"
    print(a.maxRepOpt1(text))
    text = "abcdef"
    print(a.maxRepOpt1(text))
    text = "acadaeafbbbba"
    print(a.maxRepOpt1(text))