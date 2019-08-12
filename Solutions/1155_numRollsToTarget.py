# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 10:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1155_numRollsToTarget.py
# @Software: PyCharm

'''
1155. Number of Dice Rolls With Target Sum

You have d dice, and each die has f faces numbered 1, 2, ..., f.
Return the number of possible ways (out of fd total ways) modulo 10^9 + 7
to roll the dice so the sum of the face up numbers equals target.

Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:
Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:
Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.

Constraints:
1 <= d, f <= 30
1 <= target <= 1000
'''

class Solution(object):
    memo = {}
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if (d, f, target) in self.memo:
            return self.memo[d, f, target]
        mod = 10**9 + 7
        if target < d or target > d * f:
            return 0
        if d == 0:
            return 1 if target == 0 else 0
        self.memo[d, f, target] = sum(self.numRollsToTarget(d-1, f, target-x) for x in range(1, f+1)) % mod
        return self.memo[d, f, target]

    def numRollsToTarget_1(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if d * f < target:
            return 0
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
                    k += 1
        return dp[d][target] % mod

    def numRollsToTarget_2(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if d * f <= target: return int(d * f == target)
        if d >= target: return int(d == target)
        df = [[0] * (target + 1) for _ in range(d + 1)]
        df[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                df[i][j] = df[i][j - 1] + df[i - 1][j - 1]
                if j - 1 - f >= 0:
                    df[i][j] -= df[i - 1][j - 1 - f]
        return df[d][target] % (pow(10, 9) + 7)

if __name__ == "__main__":
    a = Solution()
    d = 1
    f = 6
    target = 3
    print(a.numRollsToTarget(d, f, target))
    print(a.numRollsToTarget_1(d, f, target))
    print(a.numRollsToTarget_2(d, f, target))
    d = 2
    f = 6
    target = 7
    print(a.numRollsToTarget(d, f, target))
    print(a.numRollsToTarget_1(d, f, target))
    print(a.numRollsToTarget_2(d, f, target))
    d = 2
    f = 5
    target = 10
    print(a.numRollsToTarget(d, f, target))
    print(a.numRollsToTarget_1(d, f, target))
    print(a.numRollsToTarget_2(d, f, target))
    d = 1
    f = 2
    target = 3
    print(a.numRollsToTarget(d, f, target))
    print(a.numRollsToTarget_1(d, f, target))
    print(a.numRollsToTarget_2(d, f, target))
    d = 30
    f = 30
    target = 500
    print(a.numRollsToTarget(d, f, target))
    print(a.numRollsToTarget_1(d, f, target))
    print(a.numRollsToTarget_2(d, f, target))