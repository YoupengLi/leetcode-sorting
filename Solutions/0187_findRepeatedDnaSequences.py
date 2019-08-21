# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 9:55
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0187_findRepeatedDnaSequences.py
# @Software: PyCharm

'''
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution(object):
    # Time O(n) one pass, Space O(10*n)
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []
        dic, res, l = {}, [], 10
        for i in range(len(s) - l + 1):
            if s[i:i + l] in dic and dic[s[i:i + l]] == 1:
                res.append(s[i:i + l])
            dic[s[i:i + l]] = dic.get(s[i:i + l], 0) + 1
        return res

    def findRepeatedDnaSequences_1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []
        occmap = {}
        res = set()
        for i in range(0, len(s) - 10 + 1):
            temp = s[i:i + 10]
            if temp in occmap:
                res.add(temp)
            else:
                occmap[temp] = True
        return list(res)

    # Time O(n) one pass, Space O(4*n)
    def findRepeatedDnaSequences_2(self, s):
        res = []
        dic = {"A": 1, "C": 2, "G": 3, "T": 4}
        dicDNA = {}
        num = 1
        for i in range(len(s)):
            num = (num * 4 + dic[s[i]]) & 0XFFFFF
            if i < 9:
                continue
            if num not in dicDNA:
                dicDNA[num] = 1
            elif dicDNA[num] == 1:
                res.append(s[i - 9:i + 1])
                dicDNA[num] = 2
        return res

if __name__  == "__main__":
    a = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(a.findRepeatedDnaSequences(s))
    print(a.findRepeatedDnaSequences_1(s))
    print(a.findRepeatedDnaSequences_2(s))