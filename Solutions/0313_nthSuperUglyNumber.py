# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 20:17
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0313_nthSuperUglyNumber.py
# @Software: PyCharm

'''
313. Super Ugly Number

Write a program to find the nth super ugly number.
Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:
1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''

import heapq

class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        if n < 1:
            return 0
        res = [1]
        t = [0] * len(primes)
        nextind = 1
        while nextind < n:
            minNum = min([res[t[i]] * primes[i] for i in range(len(primes))])
            res.append(minNum)
            for i in range(len(primes)):
                while res[t[i]] * primes[i] <= minNum:
                    t[i] += 1
            nextind += 1
        return res[nextind - 1]

    def nthSuperUglyNumber_1(self, n: 'int', primes: 'List[int]') -> 'int':
        seen = {1}
        nums = []
        heap = []
        heapq.heappush(heap, 1)

        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            nums.append(curr_ugly)
            for i in primes:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return nums[-1]

    def nthSuperUglyNumber_2(self, n: 'int', primes: 'List[int]') -> 'int':
        k = len(primes)
        uglies = [1] * n
        heap = []
        seen = set()

        for p in primes:
            heapq.heappush(heap, (p, p, 0))
            seen.add(p)

        for i in range(1, n):
            # j is the index of a previous ugly number that was multiplied with prime to get the just popped ugly number
            uglies[i], prime, j = heapq.heappop(heap)
            # print(f"uglies[i]:{uglies[i]}, prime:{prime}, j:{j}")
            while prime * uglies[j] in seen: j += 1
            heapq.heappush(heap, (prime * uglies[j], prime, j))
            # print(f"heap:{heap}")
            seen.add(prime * uglies[j])

        return uglies[-1]

if __name__ == "__main__":
    a = Solution()
    n = 12
    primes = [2, 7, 13, 19]
    print(a.nthSuperUglyNumber(n, primes))
    print(a.nthSuperUglyNumber_1(n, primes))
    print(a.nthSuperUglyNumber_2(n, primes))