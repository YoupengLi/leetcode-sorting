# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 11:18
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0139_wordBreak.py
# @Software: PyCharm

'''
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak_1(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]

    def wordBreak_2(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False
        longest = len(max(wordDict, key=len))
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if j - i >= longest:
                        break
                    if s[i:j + 1] in wordDict:
                        dp[j + 1] = True
        return dp[-1]

if __name__ == "__main__":
    a = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))