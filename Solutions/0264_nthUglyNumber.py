# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 18:27
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0264_nthUglyNumber.py
# @Software: PyCharm

'''
264. Ugly Number II

Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:
1 is typically treated as an ugly number.
n does not exceed 1690.
'''

from heapq import heappop, heappush

# DP, O(1) time, O(1) space
class Ugly:
    def __init__(self):
        self.nums = nums = [1]
        i2 = i3 = i5 = 0

        # Computation takes 1690 operations
        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1

class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        if n < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        nextind = 1
        while nextind < n:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)
            while res[t2] * 2 <= minNum:
                t2 += 1
            while res[t3] * 3 <= minNum:
                t3 += 1
            while res[t5] * 5 <= minNum:
                t5 += 1
            nextind += 1
        return res[nextind - 1]

    u = Ugly()
    def nthUglyNumber_1(self, n: 'int') -> 'int':
        return self.u.nums[n - 1]

    seen = {1}
    nums = []
    heap = []
    heappush(heap, 1)

    for _ in range(1690):
        curr_ugly = heappop(heap)
        nums.append(curr_ugly)
        for i in [2, 3, 5]:
            new_ugly = curr_ugly * i
            if new_ugly not in seen:
                seen.add(new_ugly)
                heappush(heap, new_ugly)

    def nthUglyNumber_2(self, n: 'int') -> 'int':
        return self.nums[n - 1]

if __name__ == "__main__":
    a = Solution()
    n = 10
    print(a.nthUglyNumber(n))
    print(a.nthUglyNumber_1(n))
    print(a.nthUglyNumber_2(n))
    n = 1690
    print(a.nthUglyNumber(n))
    print(a.nthUglyNumber_1(n))
    print(a.nthUglyNumber_2(n))