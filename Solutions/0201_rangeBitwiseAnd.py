# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 21:34
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0201_rangeBitwiseAnd.py
# @Software: PyCharm

'''
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        直接平移m和n，每次向右移一位，直到m和n相等，记录下所有平移的次数i，然后再把m左移i位即为最终结果
        """
        if m > n:
            return
        res = 0
        while m != n:
            m >>= 1
            n >>= 1
            res += 1
        return m << res

    def rangeBitwiseAnd_1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return
        while m < n:
            n = n & (n - 1)
        return n

if __name__ == "__main__":
    a = Solution()
    m, n = 5, 7
    print(a.rangeBitwiseAnd(m, n))
    print(a.rangeBitwiseAnd_1(m, n))