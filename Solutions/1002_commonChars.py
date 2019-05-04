# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 10:43
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1002_commonChars.py
# @Software: PyCharm

'''
1002. Find Common Characters
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''

class Solution:
    def commonChars(self, A):
        if len(A) <= 0:
            return []
        res = []
        hash = []
        for i in range(len(A)):
            sub_hash = {}
            for j in A[i]:
                if j in sub_hash:
                    sub_hash[j] += 1
                else:
                    sub_hash[j] = 1
            hash.append(sub_hash)
        for i in hash[0].keys():
            flag = True
            min_num = hash[0][i]
            for j in range(1, len(A)):
                if i in hash[j]:
                    if hash[j][i] < min_num:
                        min_num = hash[j][i]
                    continue
                else:
                    flag = False
                    break
            if flag:
                while min_num > 0:
                    res.append(i)
                    min_num -= 1
        return res

if __name__ == "__main__":
    a = Solution()
    A = ["bella", "label", "roller"]
    print(a.commonChars(A))
    A = ["cool", "lock", "cook"]
    print(a.commonChars(A))