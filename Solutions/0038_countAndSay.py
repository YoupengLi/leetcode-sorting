# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0021 19:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0038_countAndSay.py
# @Software: PyCharm

'''
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''

class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        res = []
        if n == 1:
            return "1"
        else:
            res.append("1")
        for i in range(1, n):
            s = res[-1]
            temp = ""
            ind = 0
            while ind < len(s):
                num = 1
                for k in range(ind + 1, len(s)):
                    if s[k] == s[ind]:
                        num += 1
                    else:
                        break
                temp += str(num)
                temp += s[ind]
                ind += num
            res.append(temp)
        return res[-1]

    def countAndSay_1(self, n: 'int') -> 'str':
        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s

if __name__ == "__main__":
    a = Solution()
    n = 6
    res = a.countAndSay(n)
    print(res)
    res = a.countAndSay_1(n)
    print(res)