# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 9:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0115_numDistinct.py
# @Software: PyCharm

'''
115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

问题分析：
标准动态规划题目，以S = "babgbag", T = "bag"，为例，dp[i][j]表示字符串S[0:j] 中有多少个 T[0:i]，可以得到下图：
        b,j=0   a,j=1   b,j=2   g,j=3   b,j=4   a,j=5   g,j=6
b,i=0    1      1       2       2       3       3       3
a,i=1    0      1       1       1       1       4(y)    4
g,i=2    0      0       0       1       1       1(g)    ?
当i=2，j=6时，表示字符串 'babgbag' 中有多少个 'bag'，此时，要想知道现在有多少个'bag',
那么只需知道 j=5 时有多少个 'ba' 和已经有了多少个'bag', 接着再判断 S[j] ==T[i] 是否成立，
如果成立，dp[i][j] = 'ba'的个数 + 已有'bag'的个数，dp[i][j] = 已有'bag'的个数。

所以dp方程式为：dp[i][j] = dp[i][j-1] + dp[i-1][i-j] * (T[i] == S[j])
（dp[i][j-1]对应绿色方格，dp[i-1][i-j]对应黄色方格）。

dp空间压缩：
按照一列一列的计算，后一列的值只和前一列的值相关，所以，现在我们只保留一列的dp，这样就可以将2维空间压缩至1维。
'''

import collections

class Solution:
    def numDistinct(self, s: 'str', t: 'str') -> 'int':
        m, n = len(s)+1, len(t)+1
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] * (t[i-1] == s[j-1])
        return dp[-1][-1]

    def numDistinct_1(self, s: 'str', t: 'str') -> 'int':
        m, n = len(s)+1, len(t)+1
        dp = [1] + [0] * len(t)

        for j in range(1, m):
            pre = dp[:]  # pre 表示前一列的值
            for i in range(1, n):
                dp[i] = pre[i] + pre[i-1] * (t[i-1] == s[j-1])
        return dp[-1]

    def numDistinct_2(self, s: 'str', t: 'str') -> 'int':
        chars = set(t)
        dp = [1] + [0] * len(t)
        index = collections.defaultdict(list)
        for i, c in reversed(list(enumerate(t))):
            index[c].append(i+1)
        for c in s:
            if c in chars:
                print(index[c])
                for i in index[c]:
                    dp[i] += dp[i - 1]
        return dp[-1]

    def numDistinct_3(self, s: 'str', t: 'str') -> 'int':
        chars, index, dp = set(t), collections.defaultdict(list), [0] * len(t)
        for i, c in enumerate(t):
            index[c].append(i)
        for c in s:
            if c in chars:
                for i in index[c][::-1]:
                    dp[i] += dp[i - 1] if i > 0 else 1
        return dp[-1]

if __name__ == "__main__":
    a = Solution()
    S = "babgbag"
    T = "bag"
    print(a.numDistinct(S, T))
    print(a.numDistinct_1(S, T))
    print(a.numDistinct_2(S, T))
    print(a.numDistinct_3(S, T))
    S = "rabbbit"
    T = "rabbit"
    print(a.numDistinct(S, T))
    print(a.numDistinct_1(S, T))
    print(a.numDistinct_2(S, T))
    print(a.numDistinct_3(S, T))