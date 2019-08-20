# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 20:03
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0166_fractionToDecimal.py
# @Software: PyCharm

'''
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        num, den = numerator, denominator
        if not den:  # denominator is 0
            return
        if not num:  # numerator is 0
            return "0"
        res = []
        if (num < 0) ^ (den < 0):
            res.append("-")  # add the sign
        num, den = abs(num), abs(den)
        res.append(str(num // den))
        rmd = num % den
        if not rmd:
            return "".join(res)  # only has integral part
        res.append(".")  # has frational part
        dic = {}
        while rmd:
            if rmd in dic:  # the remainder recurs
                res.insert(dic[rmd], "(")
                res.append(")")
                break
            dic[rmd] = len(res)
            div, rmd = divmod(rmd * 10, den)
            res.append(str(div))
        return "".join(res)

if __name__  == "__main__":
    a = Solution()
    numerator = 1
    denominator = 2
    print(a.fractionToDecimal(numerator, denominator))
    numerator = 2
    denominator = 1
    print(a.fractionToDecimal(numerator, denominator))
    numerator = 2
    denominator = 3
    print(a.fractionToDecimal(numerator, denominator))