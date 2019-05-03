# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 0007 22:35
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0013_romanToInt.py
# @Software: PyCharm

'''
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        tab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = tab[s[0]]
        for i in range(1, len(s)):
            if (s[i] == 'V' and s[i-1] == 'I') or \
                    (s[i] == 'X' and s[i-1] == 'I') or \
                    (s[i] == 'L' and s[i - 1] == 'X') or \
                    (s[i] == 'C' and s[i - 1] == 'X') or \
                    (s[i] == 'D' and s[i - 1] == 'C') or \
                    (s[i] == 'M' and s[i - 1] == 'C'):
                res += (tab[s[i]] - tab[s[i-1]] * 2)
            else:
                res += tab[s[i]]
        return res

    def romanToInt_1(self, s: 'str') -> 'int':
        tab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if not s:
            return 0
        res = tab[s[0]]
        previous = tab[s[0]]
        for i in s[1:]:
            current = tab[i]
            res += current
            if current > previous:
                res = res - 2 * previous
            previous = current
        return res

if __name__ == "__main__":
    a = Solution()
    s = "III"
    print(a.romanToInt(s))
    print(a.romanToInt_1(s))
    s = "IV"
    print(a.romanToInt(s))
    print(a.romanToInt_1(s))
    s = "IX"
    print(a.romanToInt(s))
    print(a.romanToInt_1(s))
    s = "LVIII"
    print(a.romanToInt(s))
    print(a.romanToInt_1(s))
    s = "MCMXCIV"
    print(a.romanToInt(s))
    print(a.romanToInt_1(s))