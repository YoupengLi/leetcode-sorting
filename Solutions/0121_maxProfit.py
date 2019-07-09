# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 15:15
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0121_maxProfit.py
# @Software: PyCharm

'''
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        # Time Limit Exceeded
        if not prices:
            return 0
        res = [0] * len(prices)
        for i in range(len(prices)-1):
            res[i] = max(prices[i+1:]) - prices[i]
        return max(res)

    def maxProfit_1(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        res, mmin = 0, prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - mmin)
            mmin = min(mmin, prices[i])
        return res

    def maxProfit_2(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        res, mmin = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < mmin:
                mmin = prices[i]
            else:
                if prices[i] - mmin > res:
                    res = prices[i] - mmin
        return res

if __name__  == "__main__":
    a = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(a.maxProfit(prices))
    print(a.maxProfit_1(prices))
    print(a.maxProfit_2(prices))
    prices = [7, 6, 4, 3, 1]
    print(a.maxProfit(prices))
    print(a.maxProfit_1(prices))
    print(a.maxProfit_2(prices))
    prices = [1, 2]
    print(a.maxProfit(prices))
    print(a.maxProfit_1(prices))
    print(a.maxProfit_2(prices))