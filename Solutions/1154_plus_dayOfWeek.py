# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 9:54
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1154_plus_dayOfWeek.py
# @Software: PyCharm

'''
1154_plus. Day of the Week

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
return the day of the week.

Example 1:
Input: date = "2019-01-09"
Output: "星期三"
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: "星期日"

Example 3:
Input: date = "2003-03-01"
Output: "星期六"

Example 4:
Input: date = "2004-03-01"
Output: "星期一"

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''

class Solution(object):
    def dayOfWeek(self, date):
        """
        :type date: str
        :rtype: str
        """
        if not date:
            return
        week = {0: "星期日", 1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "星期六"}
        y, m, d = map(int, date.split("-"))
        if m == 1 or m == 2:
            m += 12
            y -= 1
        # 基姆拉尔森计算星期公式
        w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400 + 1) % 7
        return week[w]

if __name__ == "__main__":
    a = Solution()
    date = "2019-01-09"
    print(a.dayOfWeek(date))
    date = "2019-02-10"
    print(a.dayOfWeek(date))
    date = "2003-03-01"
    print(a.dayOfWeek(date))
    date = "2004-03-01"
    print(a.dayOfWeek(date))