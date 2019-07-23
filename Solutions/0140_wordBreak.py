# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 15:47
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0140_wordBreak.py
# @Software: PyCharm

'''
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if not s or not wordDict:
            return []
        res = []
        self.dfs(s, wordDict, "", res)
        return res

    # Before we do dfs, we check whether the remaining string
    # can be splitted by using the dictionary,
    # in this way we can decrease unnecessary computation greatly.
    def dfs(self, s: 'str', wordDict: 'List[str]', path: 'str', res: 'List[str]'):
        if not s:
            res.append(path[:-1])
            return
        if self.check(s, wordDict):  # prunning
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    # dic.remove(s[:i])
                    self.dfs(s[i:], wordDict, path + s[:i] + " ", res)

    # DP code to check whether a string can be splitted by using the
    # dic, this is the same as word break I.
    def check(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]

    def wordBreak_1(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if not s or not wordDict:
            return []
        if not self.check_1(s, wordDict):
            return []

        n = len(s)
        word_dict = set(wordDict)
        max_len = max(len(word) for word in word_dict)
        min_len = min(len(word) for word in word_dict)

        def dp(i):
            if i >= n:
                return [""]
            res = []
            ed_left = i + min_len
            ed_right = min(i + max_len, n)

            for ed in range(ed_left, ed_right + 1):
                if s[i:ed] in word_dict and dp(ed):
                    res += [s[i:ed] + ' ' + rest if rest else s[i:ed] for rest in dp(ed)]
            return res

        return dp(0)

    def check_1(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]

    def wordBreak_2(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if not s or not wordDict:
            return []
        wordDict = set(wordDict)
        backup = {}
        self.res = []

        def dfs_2(s: 'str') -> 'List[str]':
            if not s:
                return ['']
            if s not in backup:
                backup[s] = []
                for i in range(1, len(s) + 1):
                    word = s[:i]
                    if word in wordDict:
                        sentences = dfs_2(s[i:])
                        for ss in sentences:
                            backup[s].append(word + ' ' + ss)
            return backup[s]

        dfs_2(s)
        return [bu[:-1] for bu in backup[s]]

if __name__ == "__main__":
    a = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(a.wordBreak(s, wordDict))
    print(a.wordBreak_1(s, wordDict))
    print(a.wordBreak_2(s, wordDict))