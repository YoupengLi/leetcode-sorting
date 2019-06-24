# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 23:03
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0096_numTrees.py
# @Software: PyCharm

'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

import math
class Solution:
    def numTrees(self, n: 'int') -> 'int':
        if n == 0 or n == 1:
            return 1
        res = 0
        for i in range(n):
            leftTrees = self.numTrees(i)
            rightTrees = self.numTrees(n-i-1)
            res += leftTrees * rightTrees
        return res

    def numTrees_1(self, n: 'int') -> 'int':
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[-1]

    def numTrees_2(self, n: 'int') -> 'int':
        # Catalan Number (2n)!/((n+1)! * n!)
        return int(math.factorial(2*n)/(math.factorial(n+1) * math.factorial(n)))

    def numTrees_3(self, n: int) -> int:
        if n < 1:
            return 0
        dp = [1, 1]
        for i in range(2, n + 1):
            dp_i = 0
            for j in range(1, i + 1):
                dp_i += dp[j - 1] * dp[i - j]
            dp.append(dp_i)
        return dp[n]

if __name__ == "__main__":
    a = Solution()
    n = 17
    # print(a.numTrees(n))
    print(a.numTrees_1(n))
    print(a.numTrees_2(n))
    print(a.numTrees_3(n))