# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 14:29
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0131_partition.py
# @Software: PyCharm

'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s: 'str', path: 'List[str]', res: 'List[List[str]]') -> 'None':
        if not s:
            res.append(path[:])
            return  # backtracking
        for i in range(1, len(s) + 1):
            if self.isPar(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:], path, res)
                path.pop()  # simulate stack here

    def isPar(self, s: 'str') -> 'bool':
        return s == s[::-1]

    def partition_1(self, s: 'str') -> 'List[List[str]]':
        res = []
        self.dfs_1(s, [], res)
        return res

    def dfs_1(self, s: 'str', path: 'List[str]', res: 'List[List[str]]') -> 'None':
        if not s:
            res.append(path[:])
            return  # backtracking
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                path.append(s[:i])
                self.dfs_1(s[i:], path, res)
                path.pop()  # simulate stack here

    def partition_2(self, s: 'str') -> 'List[List[str]]':
        res = []

        def dfs(s: 'str', path: 'List[str]', res: 'List[List[str]]') -> 'None':
            if not s:
                res.append(path[:])
                return  # backtracking
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()  # simulate stack here

        dfs(s, [], res)
        return res


    def partition_3(self, s: 'str') -> 'List[List[str]]':
        if not s:
            return []

        # Each list of lists is the set of palindromes
        # for the string ending at char s[key-1]
        dp = {0: [[]], 1: [[s[0]]]}

        # Get partitioned palindromes for substr ending at char i
        for i in range(1, len(s)):
            dp[i + 1] = []

            # Sub-string start positions from 0 to i
            for j in range(0, i + 1):

                # If the substr is a palindrome
                substr = s[j:i + 1]
                if substr == substr[::-1]:
                    # Get sols ending just before it starts
                    # Add the sol with the new pal to the
                    # palindromic-partitioned substrings for
                    # the substrings ending at i
                    for sol in dp[j]:
                        dp[i + 1].append(sol + [substr])

        # Return a list containing the lists of palindromic
        # substrings that have length s.
        return dp[len(s)]

if __name__  == "__main__":
    a = Solution()
    s = "aab"
    print(a.partition(s))
    print(a.partition_1(s))
    print(a.partition_2(s))
    print(a.partition_3(s))