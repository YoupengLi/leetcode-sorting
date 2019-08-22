# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 8:11
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0191_hammingWeight.py
# @Software: PyCharm

'''
191. Number of 1 Bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case,
the input will be given as signed integer type and should not affect your implementation,
as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
If this function is called many times, how would you optimize it?
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        res, tmp = 0, 1
        for i in range(32):
            if n & tmp:
                res += 1
            tmp <<= 1
        return res

    def hammingWeight_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        mybin = bin(n)
        return mybin.count('1')

    def hammingWeight_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            if (n ^ (n - 1)) == 1:
                count += 1
            n = n >> 1
        return count

if __name__ == "__main__":
    a = Solution()
    n = 11
    print(a.hammingWeight(n))
    print(a.hammingWeight_1(n))
    print(a.hammingWeight_2(n))
    n = 128
    print(a.hammingWeight(n))
    print(a.hammingWeight_1(n))
    print(a.hammingWeight_2(n))