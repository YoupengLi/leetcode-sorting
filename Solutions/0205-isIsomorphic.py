# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 9:12
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0205-isIsomorphic.py
# @Software: PyCharm

'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic_2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # print([s.find(i) for i in s])
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic_3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.find, s)) == list(map(t.find, t))

    def isIsomorphic_4(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        # 别人的聪明方法：用memo来映射，用set来记录是否见过
        memo = {}
        rep = set()
        for i in range(len(s)):
            if s[i] not in memo:
                if t[i] in rep:
                    return False
                memo[s[i]] = t[i]
                rep.add(t[i])
            else:
                if t[i] != memo[s[i]]:
                    return False
        return True


if __name__ == "__main__":
    a = Solution()
    s = "egg"
    t = "add"
    print(a.isIsomorphic(s, t))
    print(a.isIsomorphic_1(s, t))
    print(a.isIsomorphic_2(s, t))
    print(a.isIsomorphic_3(s, t))
    print(a.isIsomorphic_4(s, t))