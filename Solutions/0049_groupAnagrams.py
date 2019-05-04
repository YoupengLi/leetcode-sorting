# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 17:28
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0049_groupAnagrams.py
# @Software: PyCharm

'''
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''
import collections
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        val = ans.values()
        res = []
        for i in val:
            res.append(i)
        return res

if __name__ == "__main__":
    a = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = a.groupAnagrams(strs)
    print(res)