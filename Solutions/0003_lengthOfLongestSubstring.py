# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 0016 下午 5:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0003_lengthOfLongestSubstring.py
# @Software: PyCharm

'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max_count = 0
        # dict1储存的是所有不重复的字符串的最新的index
        # abcabcbb 运行3步：a:0, b:1, c:2
        # abcabcbb 运行4步：a:3, b:1, c:2
        dict1 = {}
        leftside = -1
        for index, ch in enumerate(s):
            if (ch in dict1) and (leftside < dict1[ch]):
                leftside = dict1[ch]
            new_count = index - leftside
            if new_count > max_count:
                max_count = new_count
            dict1[ch] = index
        # 最后判断leftside~end的长度与max_count的大小
        new_count = len(s) - leftside - 1
        if new_count > max_count:
            max_count = new_count
        return max_count

if __name__ == "__main__":
    a = Solution()
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    print(a.lengthOfLongestSubstring(s1))
    print(a.lengthOfLongestSubstring(s2))
    print(a.lengthOfLongestSubstring(s3))
