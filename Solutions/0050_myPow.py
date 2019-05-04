# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 20:16
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0050_myPow.py
# @Software: PyCharm

'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
'''

class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':
        m = abs(n)
        ans = 1.0
        while m:
            if m & 1:
                ans *= x
            x *= x
            m >>= 1
        return ans if n >= 0 else 1 / ans

if __name__ == "__main__":
    a = Solution()
    x = 2.00000
    n = -20
    res = a.myPow(x, n)
    print(res)