# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 21:45
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0172_trailingZeroes.py
# @Software: PyCharm

'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

注意:25=5*5是有两个5的因子；125=5*5*5有3个5的因子。比如，计算135!末尾0的个数。
首先135/5 = 27，说明135以内有27个5的倍数；27/5=5，说明135以内有5个25的倍数；
5/5=1，说明135以内有1个125的倍数。
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        res = 0
        while n != 0:
            res += n // 5
            n //= 5
        return res

if __name__  == "__main__":
    a = Solution()
    n = 3
    print(a.trailingZeroes(n))
    n = 5
    print(a.trailingZeroes(n))
    n = 2 ** 31
    print(a.trailingZeroes(n))