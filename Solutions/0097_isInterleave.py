# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 9:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0097_isInterleave.py
# @Software: PyCharm

'''
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''


class Solution:
    def isInterleave(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        if not s1:
            return (s2 == s3)
        elif not s2:
            return (s1 == s3)
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and dp[i][j - 1] == 1 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = 1
                elif j == 0 and dp[i - 1][j] == 1 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = 1
                elif (dp[i - 1][j] == 1 and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] == 1 and s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = 1
        return dp[-1][-1] == 1

    def isInterleave_1(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        matrix = dict()

        def dfs(s1, s1_pos, s2, s2_pos, s3, s3_pos):
            if s1_pos == len(s1) and s2_pos == len(s2):
                return s3_pos == len(s3)
            elif s1_pos == len(s1):
                return s2[s2_pos:] == s3[s3_pos:]
            elif s2_pos == len(s2):
                return s1[s1_pos:] == s3[s3_pos:]

            if (s1_pos, s2_pos) in matrix:
                return matrix[(s1_pos, s2_pos)]

            res = False
            if s1[s1_pos] == s3[s3_pos]:
                res = dfs(s1, s1_pos + 1, s2, s2_pos, s3, s3_pos + 1)
            if not res and s2[s2_pos] == s3[s3_pos]:
                res = dfs(s1, s1_pos, s2, s2_pos + 1, s3, s3_pos + 1)
            matrix[(s1_pos, s2_pos)] = res
            return res

        return dfs(s1, 0, s2, 0, s3, 0)

if __name__ == "__main__":
    a = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(a.isInterleave(s1, s2, s3))
    print(a.isInterleave_1(s1, s2, s3))
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(a.isInterleave(s1, s2, s3))
    print(a.isInterleave_1(s1, s2, s3))
    s1 = ""
    s2 = ""
    s3 = "a"
    print(a.isInterleave(s1, s2, s3))
    print(a.isInterleave_1(s1, s2, s3))
    s1 = "a"
    s2 = ""
    s3 = "a"
    print(a.isInterleave(s1, s2, s3))
    print(a.isInterleave_1(s1, s2, s3))
    s1 = "a"
    s2 = "b"
    s3 = "ab"
    print(a.isInterleave(s1, s2, s3))
    print(a.isInterleave_1(s1, s2, s3))
    s1 = "aabaac"
    s2 = "aadaaeaaf"
    s3 = "aadaaeaabaacaaf"
    print(a.isInterleave(s1, s2, s3))
    print(a.isInterleave_1(s1, s2, s3))