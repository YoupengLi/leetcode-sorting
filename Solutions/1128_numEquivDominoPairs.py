# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 10:37
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1128_numEquivDominoPairs.py
# @Software: PyCharm

'''
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
if and only if either (a==c and b==d), or (a==d and b==c) - that is,
one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Constraints:
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
'''

from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: 'List[List[int]]') -> 'int':
        if not dominoes:
            return 0
        res = 0
        for i in range(len(dominoes)):
            for j in range(i+1, len(dominoes)):
                if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or \
                    (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
                    res += 1
        return res

    def numEquivDominoPairs_1(self, dominoes: 'List[List[int]]') -> 'int':
        if not dominoes:
            return 0
        dic = {}
        res = 0
        for i in dominoes:
            if i[0] > i[1]:
                i[0], i[1] = i[1], i[0]
            if (i[0], i[1]) not in dic.keys():
                dic[(i[0], i[1])] = 1
            else:
                dic[(i[0], i[1])] += 1
        for i in dic.values():
            res += i * (i - 1) // 2
        return res

    def numEquivDominoPairs_2(self, dominoes: 'List[List[int]]') -> 'int':
        dicti, res = defaultdict(int), 0
        for i, j in dominoes:
            dicti[(i, j)] += 1
        for key in dicti:
            res += (dicti[key] - 1) * dicti[key] // 2
            if key[0] < key[1] and (key[1], key[0]) in dicti:
                res += dicti[key] * dicti[(key[1], key[0])]
        return res

    def numEquivDominoPairs_3(self, dominoes: 'List[List[int]]') -> 'int':
        counter = defaultdict(int)
        for lst in dominoes:
            counter[tuple(sorted(lst))] += 1
        res= 0
        for v in counter.values():
            if v >= 2:
                res += v * (v - 1)
        return res // 2

if __name__ == "__main__":
    a = Solution()
    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    print(a.numEquivDominoPairs(dominoes))
    print(a.numEquivDominoPairs_1(dominoes))
    print(a.numEquivDominoPairs_2(dominoes))
    print(a.numEquivDominoPairs_3(dominoes))
    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    print(a.numEquivDominoPairs(dominoes))
    print(a.numEquivDominoPairs_1(dominoes))
    print(a.numEquivDominoPairs_2(dominoes))
    print(a.numEquivDominoPairs_3(dominoes))