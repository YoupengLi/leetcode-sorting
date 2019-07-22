# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 11:52
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1131_maxAbsValExpr.py
# @Software: PyCharm

'''
1131. Maximum of Absolute Value Expression

Given two arrays of integers with equal lengths, return the maximum value of:
|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
where the maximum is taken over all 0 <= i, j < arr1.length.

Example 1:
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13

Example 2:
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20

Constraints:
2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
'''

class Solution:
    def maxAbsValExpr(self, arr1: 'List[int]', arr2: 'List[int]') -> 'int':
        if not arr1:
            return 0
        tmp = [[0]*len(arr1) for _ in range(len(arr1))]
        for i in range(len(arr1)):
            for j in range(i+1, len(arr1)):
                tmp[i][j] += abs(arr1[i] - arr1[j])
                tmp[i][j] += abs(arr2[i] - arr2[j])
                tmp[i][j] += abs(i - j)
        return max(max(row) for row in tmp)

    def maxAbsValExpr_1(self, arr1: 'List[int]', arr2: 'List[int]') -> 'int':
        if not arr1:
            return 0
        res = 0
        for i in range(len(arr1)):
            tmp = [0] * len(arr1)
            for j in range(i+1, len(arr1)):
                tmp[j] += abs(arr1[i] - arr1[j])
                tmp[j] += abs(arr2[i] - arr2[j])
                tmp[j] += abs(i - j)
            res = max(res, max(tmp))
        return res

    def maxAbsValExpr_2(self, arr1: 'List[int]', arr2: 'List[int]') -> 'int':
        max1 = max2 = max3 = max4 = float('-inf')
        min1 = min2 = min3 = min4 = float('inf')

        for i in range(len(arr1)):
            tmp1 = arr1[i] - arr2[i] - i
            max1 = max(max1, tmp1)
            min1 = min(min1, tmp1)

            tmp2 = arr1[i] + arr2[i] - i
            max2 = max(max2, tmp2)
            min2 = min(min2, tmp2)

            tmp3 = arr1[i] + arr2[i] + i
            max3 = max(max3, tmp3)
            min3 = min(min3, tmp3)

            tmp4 = arr1[i] - arr2[i] + i
            max4 = max(max4, tmp4)
            min4 = min(min4, tmp4)

        return max((max1 - min1), (max2 - min2), (max3 - min3), (max4 - min4))

    def maxAbsValExpr_3(self, arr1: 'List[int]', arr2: 'List[int]') -> 'int':
        res, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        return res

if __name__ == "__main__":
    a = Solution()
    arr1 = [1, 2, 3, 4]
    arr2 = [-1, 4, 5, 6]
    print(a.maxAbsValExpr(arr1, arr2))
    print(a.maxAbsValExpr_1(arr1, arr2))
    print(a.maxAbsValExpr_2(arr1, arr2))
    print(a.maxAbsValExpr_3(arr1, arr2))
    arr1 = [1, -2, -5, 0, 10]
    arr2 = [0, -2, -1, -7, -4]
    print(a.maxAbsValExpr(arr1, arr2))
    print(a.maxAbsValExpr_1(arr1, arr2))
    print(a.maxAbsValExpr_2(arr1, arr2))
    print(a.maxAbsValExpr_3(arr1, arr2))
    arr1 = [0, 7, 5, -3, 8, 3, 5, 4]
    arr2 = [-5, 8, 5, 3, 0, 1, -5, 0]
    print(a.maxAbsValExpr(arr1, arr2))
    print(a.maxAbsValExpr_1(arr1, arr2))
    print(a.maxAbsValExpr_2(arr1, arr2))
    print(a.maxAbsValExpr_3(arr1, arr2))
    arr1 = [-5, 1, 4, -10, -7, -5, -2, -7, -2, 10, 1, -8, -8, -8, 2, -3, -5, -3, -4, 3]
    arr2 = [3, 9, -6, 6, -8, -2, 8, 8, -6, 7, 5, 0, -4, 5, -10, -5, -9, -10, 8, 10]
    print(a.maxAbsValExpr(arr1, arr2))
    print(a.maxAbsValExpr_1(arr1, arr2))
    print(a.maxAbsValExpr_2(arr1, arr2))
    print(a.maxAbsValExpr_3(arr1, arr2))
    arr1 = [854632, 428107, -704467, 832706, -319640, -365224, -947863, 729070, -312850, 36528, 311684, -100859, -177471,
     -558426, -661854, 668679, -87676, -646544, 30934, -349421, 165215, -183902, 417453, 86953, 388125, -797836, 115123,
     156068, -479616, 313614]
    arr2 = [854632, 428107, -704467, 832706, -319640, -365224, -947863, 729070, -312850, 36528, 311684, -100859,
            -177471,
            -558426, -661854, 668679, -87676, -646544, 30934, -349421, 165215, -183902, 417453, 86953, 388125, -797836,
            115123,
            156068, -479616, 313614]
    print(a.maxAbsValExpr(arr1, arr2))
    print(a.maxAbsValExpr_1(arr1, arr2))
    print(a.maxAbsValExpr_2(arr1, arr2))
    print(a.maxAbsValExpr_3(arr1, arr2))