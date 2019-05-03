# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 0007 07:50
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0008_myAtoi.py
# @Software: PyCharm

'''
8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and
have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values,
INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
'''

class Solution:
    def myAtoi(self, s: 'str') -> 'int':
        str = str.lstrip()
        if len(str) <= 0:
            return 0
        numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
                   '6':6, '7':7, '8':8, '9':9}
        if str[0] != '+' and str[0] != '-' and str[0] not in numbers.keys():
            return 0

        if str[0] == '+' or str[0] == '-':
            s = str[1:]
        else:
            s = str[:]

        num = []
        for i in s:
            if i in numbers.keys():
                num.append(numbers[i])
            else:
                break

        res = 0
        for i in num:
            res = res*10 + i
        if str[0] == '-':
            res = 0 - res
        maxint = 2147483647
        minint = -2147483648
        if res > maxint:
            return maxint
        if res < minint:
            return minint
        return res

    def myAtoi_1(self, s: 'str') -> 'int':
        start = 0
        if s == "":
            return 0
        number_s = ''
        s = s.lstrip()
        for l in s:
            if start == 0:
                if l == '-' or ('0' <= l <= '9'):
                    start = 1
                    number_s = number_s + l
                elif l == "+":
                    start = 1
                    continue
                else:
                    return 0
            elif start == 1:
                if '0' <= l <= '9':
                    number_s = number_s + l
                else:
                    break
        if number_s == '' or number_s == '-':
            return 0
        elif -2 ** 31 <= int(number_s) < 2 ** 31:
            return int(number_s)
        elif int(number_s) >= 2 ** 31:
            return 2 ** 31 - 1
        elif int(number_s) < -2 ** 31:
            return -2 ** 31
        else:
            return 0

if __name__ == "__main__":
    a = Solution()
    str1 = "42"
    str2 = "  -42"
    str3 = "4193 with words"
    str4 = "words and 987"
    str5 = "-91283472332"
    print(a.myAtoi(str1))
    print(a.myAtoi_1(str1))
    print(a.myAtoi(str2))
    print(a.myAtoi_1(str2))
    print(a.myAtoi(str3))
    print(a.myAtoi_1(str3))
    print(a.myAtoi(str4))
    print(a.myAtoi_1(str4))
    print(a.myAtoi(str5))
    print(a.myAtoi_1(str5))