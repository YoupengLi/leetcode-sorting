# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 21:08
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0123_maxProfit.py
# @Software: PyCharm

'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

解题思路：动态规划
使用两个数组，forw和back；
forw[i]表示从0到i的最优买卖值（低买高卖，为正）。需要一次从左往右遍历。
back[i]表示从m-1到i的最差买卖值（高买低卖，为负）。需要一次从右往左遍历。
再对应元素相减：forw[i]-back[i]的最大值即解。
'''

import sys

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max

    def maxProfit_1(self, prices: 'List[int]') -> 'int':
        one_buy = two_buy = sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        return two_profit

if __name__ == "__main__":
    a = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(a.maxProfit(prices))
    print(a.maxProfit_1(prices))
    prices = [1, 2, 3, 4, 5]
    print(a.maxProfit(prices))
    print(a.maxProfit_1(prices))
    prices = [7, 6, 4, 3, 1]
    print(a.maxProfit(prices))
    print(a.maxProfit_1(prices))