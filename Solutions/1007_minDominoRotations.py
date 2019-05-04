# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0010 11:50
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1007_minDominoRotations.py
# @Software: PyCharm

'''
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same,
or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:
1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
'''

class Solution:
    def minDominoRotations(self, A: 'list[int]', B: 'list[int]') -> 'int':
        if not A or len(A) <= 0:
            return 0
        dict1 = {}
        for i in A:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in B:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        val = max(dict1, key=dict1.get)
        if dict1[val] < len(A):
            return -1
        count_A = 0
        count_B = 0
        for i in range(len(A)):
            if A[i] != val:
                count_A += 1
                if B[i] != val:
                    return -1
            else:
                continue

        for i in range(len(B)):
            if B[i] != val:
                count_B += 1
                if A[i] != val:
                    return -1
            else:
                continue
        res = min(count_A, count_B)
        return res

if __name__ == "__main__":
    a = Solution()
    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    print(a.minDominoRotations(A, B))