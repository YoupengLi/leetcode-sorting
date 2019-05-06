# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 22:25
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0070_climbStairs.py
# @Software: PyCharm

'''
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        res = [1, 2]
        while len(res) < n:
            res.append(res[-1] + res[-2])
        return res[n - 1]

    def climbStairs_1(self, n: 'int') -> 'int':
        if n <= 1:
            return 1

        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1

        for stair in range(2, n + 1):
            table[stair] = table[stair - 1] + table[stair - 2]

        return table[n]

    def climbStairs_2(self, n: 'int') -> 'int':
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

    def climbStairs_3(self, n: 'int') -> 'int':
        res = [1, 2]
        for i in range(2, n):
            res.append(res[-1] + res[-2])
        return res[n - 1]

if __name__ == "__main__":
    a = Solution()
    n = 1
    print(a.climbStairs_3(n))
