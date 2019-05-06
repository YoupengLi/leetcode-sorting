# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 21:51
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0069_mySqrt.py
# @Software: PyCharm

'''
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and
only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                r = mid - 1
            else:
                l = mid + 1

    def mySqrt_1(self, x: 'int') -> 'int':
        return int(pow(x, 0.5))

if __name__ == "__main__":
    a = Solution()
    x = 2147395599
    print(a.mySqrt(x))
    print(a.mySqrt_1(x))