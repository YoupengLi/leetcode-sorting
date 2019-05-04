# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0010 10:31
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1005_largestSumAfterKNegations.py
# @Software: PyCharm

'''
1005. Maximize Sum Of Array After K Negations
Given an array A of integers, we must modify the array in the following way:
we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.
 (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:
Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:
Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].


Note:
1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
'''

class Solution:
    def largestSumAfterKNegations(self, A: 'list[int]', K: 'int') -> 'int':
        if not A or len(A) <= 0:
            return 0
        A.sort()
        ge = [i for i in A if i >= 0]
        l = [i for i in A if i < 0]

        if len(l) >= K:
            for i in range(K):
                l[i] = -l[i]
            return sum(l) + sum(ge)
        elif len(l) == 0:
            if K % 2 == 0:
                return sum(ge)
            else:
                return sum(ge) - 2 * ge[0]
        else:
            if (K-len(l)) % 2 == 0:
                return -sum(l) + sum(ge)
            else:
                min_abs = -l[len(l) - 1]
                if ge[0] < min_abs:
                    min_abs = ge[0]
                return -sum(l) + sum(ge) - 2 * min_abs

if __name__ == "__main__":
    a = Solution()
    A = [1, 3, 2, 6, 7, 9]
    K = 5
    print(a.largestSumAfterKNegations(A, K))