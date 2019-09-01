# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 8:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0204_countPrimes.py
# @Software: PyCharm

'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        count = 0
        for i in range(2, n):
            if self.isPrimes(i):
                count += 1
        return count

    def isPrimes(self, num):
        sqrt = int(math.sqrt(num))
        for i in range(2, sqrt+1):
            if num % i == 0:
                return False
        return True

    def countPrimes_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(2, (n - 1) // i + 1):
                    res[i * j] = False
        return sum(res)

    def countPrimes_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    def countPrimes_3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        import numpy as np
        l = np.ones(n, dtype=bool)
        l[4::2] = False
        for i in range(3, int(n ** 0.5) + 1, 2):
            l[i * i::i] = False
        return int(np.sum(l[2:]))

if __name__ == "__main__":
    a = Solution()
    n = 999983
    # print(a.countPrimes(n))
    print(a.countPrimes_1(n))
    print(a.countPrimes_2(n))
    print(a.countPrimes_3(n))