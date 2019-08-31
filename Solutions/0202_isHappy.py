# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 22:32
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0202_isHappy.py
# @Software: PyCharm

'''
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        dic = {}
        key = n
        while True:
            key = list(map(int, str(key)))
            tmp = [i ** 2 for i in key]
            key = sum(tmp)
            if key == 1:
                return True
            elif key not in dic:
                dic[key] = 1
            else:
                return False

    def isHappy_1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while n:
            if n == 1:
                return True
            elif n not in dic:
                dic[n] = 1
            else:
                return False
            n = list(map(int, str(n)))
            tmp = [i ** 2 for i in n]
            n = sum(tmp)

    def isHappy_2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while n:
            if n == 1:
                return True
            elif n not in dic:
                dic[n] = 1
            else:
                return False
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp

if __name__ == "__main__":
    a = Solution()
    n = 19
    print(a.isHappy(n))
    print(a.isHappy_1(n))
    print(a.isHappy_2(n))