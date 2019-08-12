# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 10:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1154_dayOfYear.py
# @Software: PyCharm

'''
1154. Day of the Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41

Example 3:
Input: date = "2003-03-01"
Output: 60

Example 4:
Input: date = "2004-03-01"
Output: 61

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''

from datetime import datetime

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        if not date:
            return 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = list(map(int, date.split("-")))
        if date[0] % 4 == 0 and date[0] % 100 != 0 or date[0] % 400 == 0:
            days[1] = 29
        res = sum(days[:date[1]-1]) + date[2]
        return res

    def dayOfYear_1(self, date):
        """
        :type date: str
        :rtype: int
        """
        if not date:
            return 0
        Y, M, D = map(int, date.split("-"))
        return (datetime(Y, M, D) - datetime(Y, 1, 1)).days + 1

if __name__ == "__main__":
    a = Solution()
    date = "2019-01-09"
    print(a.dayOfYear(date))
    print(a.dayOfYear_1(date))
    date = "2019-02-10"
    print(a.dayOfYear(date))
    print(a.dayOfYear_1(date))
    date = "2003-03-01"
    print(a.dayOfYear(date))
    print(a.dayOfYear_1(date))
    date = "2004-03-01"
    print(a.dayOfYear(date))
    print(a.dayOfYear_1(date))