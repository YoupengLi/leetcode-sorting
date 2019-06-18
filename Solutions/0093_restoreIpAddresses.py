# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 16:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0093_restoreIpAddresses.py
# @Software: PyCharm

'''
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s: 'str', index: 'int', path: 'str', res: 'list[str]'):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return      # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                # choose one digit
                if i == 1:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                # choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                # choose three digits, the first one should not be "0" and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)

if __name__ == "__main__":
    a = Solution()
    s = "25525511135"
    print(a.restoreIpAddresses(s))