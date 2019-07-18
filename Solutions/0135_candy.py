# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 0018 09:54
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0135_candy.py
# @Software: PyCharm

'''
135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''


class Solution:
    def candy(self, ratings: 'List[int]') -> 'int':
        if not ratings:
            return 0
        res = [1] * len(ratings)
        lbase, rbase = 1, 1

        for i in range(1, len(ratings)):  # 从左向右扫描
            lbase = lbase + 1 if ratings[i] > ratings[i - 1] else 1
            res[i] = lbase

        for i in range(len(ratings) - 2, -1, -1):  # 从右向左扫描
            rbase = rbase + 1 if ratings[i] > ratings[i + 1] else 1
            res[i] = max(rbase, res[i])
        return sum(res)

    def candy_1(self, ratings: 'List[int]') -> 'int':
        peak = down = up = 0
        res = 1
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                up += 1
                down = 0
                peak = up
                res += 1 + up
            elif ratings[i - 1] == ratings[i]:
                up = down = peak = 0
                res += 1
            else:
                up = 0
                down += 1
                res += 1 + down + ((-1) if peak >= down else 0)
        return res

if __name__ == "__main__":
    a = Solution()
    ratings = [1, 0, 2]
    print(a.candy(ratings))
    print(a.candy_1(ratings))
    ratings = [1, 2, 2]
    print(a.candy(ratings))
    print(a.candy_1(ratings))
    ratings = [1, 2, 3, 2, 1, 0]
    print(a.candy(ratings))
    print(a.candy_1(ratings))