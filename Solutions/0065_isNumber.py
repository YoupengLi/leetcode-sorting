# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 9:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0065_isNumber.py
# @Software: PyCharm

'''
65. Valid Number

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
'''

class Solution:
    def isNumber(self, s: 'str') -> 'bool':
        s = s.strip()
        if not s or len(s) <= 0:
            return False
        num_dict = {'0':1, '1':1, '2':1, '3':1, '4':1, '5':1,'6':1, '7':1, '8':1, '9':1}
        my_dict1 = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '+': 1, '-': 1,
                    '.': 1}
        my_dict2 = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '.': 1, 'e': 1,
                    '+': 1, '-': 1}
        for i in range(len(s)):
            if s[i] not in my_dict2.keys():
                return False
            if s[i] == "+" or s[i] == "-":
                if i == 0:
                    continue
                elif s[i-1] == "e" and s[i] == "-" and i < len(s)-1:
                    continue
                elif s[i - 1] == "e" and s[i] == "+" and i < len(s) - 1:
                    continue
                else:
                    return False
            if i == 0:
                if s[i] not in my_dict1.keys():
                    return False
            elif i == len(s)-1:
                if s[i] not in num_dict.keys() and s[i] != '.':
                    return False
        if s.count(".") > 1 or s.count("e") > 1:
            return False
        if s.count(".") == 1:
            if s.count("e") == 1:
                if s.index(".") > s.index("e"):
                    return False
                else:
                    flag = False
                    for i in s[:s.index("e")]:
                        if i in num_dict.keys():
                            flag = True
                            break
                        else:
                            continue
                    if not flag:
                        return False
                    else:
                        return True
            if s.count("e") == 0:
                flag = False
                for i in s:
                    if i in num_dict.keys():
                        flag = True
                        break
                    else:
                        continue
                if not flag:
                    return False
                else:
                    return True
        if s.count(".") == 0 and s.count("e") == 1:
            flag = False
            for i in s[:s.index("e")]:
                if i in num_dict.keys():
                    flag = True
                    break
                else:
                    continue
            if not flag:
                return False
            else:
                return True
        return True

    def isNumber_1(self, s: 'str') -> 'bool':
        try:
            float(s.strip())
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    a = Solution()
    print(a.isNumber("0"))
    print(a.isNumber(" 0.1 "))
    print(a.isNumber("abc"))
    print(a.isNumber("1 a"))
    print(a.isNumber("2e10"))
    print(a.isNumber(" -90e3   "))
    print(a.isNumber(" 1e"))
    print(a.isNumber("e3"))
    print(a.isNumber(" 6e-1"))
    print(a.isNumber(" 99e2.5 "))
    print(a.isNumber("53.5e93"))
    print(a.isNumber(" --6 "))
    print(a.isNumber("-+3"))
    print(a.isNumber("95a54e53"))
    print(a.isNumber("."))
    print(a.isNumber("3."))
    print(a.isNumber("3.e-5"))
    print(a.isNumber(".e-5"))
    print(a.isNumber("-."))
    print(a.isNumber(". 1"))
    print(a.isNumber("-e58"))
    print(a.isNumber(" 005047e+6"))
    print(a.isNumber_1(" 005047e+6"))
