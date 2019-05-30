# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 0021 10:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0072_minDistance.py
# @Software: PyCharm

'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

解题思路：采用动态规划算法
字符串编辑距离 ——> Levenshtein距离：利用字符操作，把字符串A转换成字符串B所需要的最少操作次数
if i==0 and j==0,   edit(i,j)=0
if i==0 and j>0,    edit(i,j)=j
if i>0  and j==0,   edit(i,j)=i
if i>=1 and j>=1,   edit(i,j)=min{edit(i-1,j)+1, edit(i,j-1)+1, edit(i-1,j-1)+f(i,j)}
其中，当第一个字符串的第i个字符不等于第二个字符串的第j个字符时，f(i,j)=1,否则，f(i,j)=0

'''
import heapq
class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1): dp[i][0] = i
        for j in range(1, len2 + 1): dp[0][j] = j
        # dp
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else dp[i - 1][j - 1] + 1)
        return dp[len1][len2]


    def minDistance_1(self, word1: 'str', word2: 'str') -> 'int':
        heap = [(0, word1, word2)]
        seen = set()
        n = 0
        while heap:
            dis, w1, w2 = heapq.heappop(heap)
            if w1 == w2: return dis
            if not (w1, w2) in seen:
                seen.add((w1, w2))
                while w1 and w2 and w1[-1] == w2[-1]:
                    w1 = w1[:-1]
                    w2 = w2[:-1]
                else:
                    heapq.heappush(heap, (dis + 1, w1[:-1], w2))
                    if w2:
                        heapq.heappush(heap, (dis + 1, w1, w2[:-1]))
                    if w1 and w2:
                        heapq.heappush(heap, (dis + 1, w1[:-1], w2[:-1]))

if __name__ == "__main__":
    a = Solution()
    word1 = "horse"
    word2 = "ros"
    res = a.minDistance(word1, word2)
    print(res)
    word1 = "intention"
    word2 = "execution"
    res = a.minDistance(word1, word2)
    print(res)
    word1 = ""
    word2 = ""
    res = a.minDistance(word1, word2)
    print(res)
    word1 = ""
    word2 = "a"
    res = a.minDistance(word1, word2)
    print(res)
    word1 = "dinitrophenylhydrazine"
    word2 = "benzalphenylhydrazone"
    res = a.minDistance(word1, word2)
    print(res)
    res = a.minDistance_1(word1, word2)
    print(res)