# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 20:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0089_grayCode.py
# @Software: PyCharm

'''
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1

Example 2:
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
'''

class Solution:
    def grayCode(self, n: 'int') -> 'List[int]':
        return [0] if n == 0 else self.grayCode(n-1) + [i + (1<<(n-1)) for i in reversed(self.grayCode(n-1))]

    def grayCode_1(self, n: 'int') -> 'List[int]':
        if n == 0:
            return [0]
        else:
            res = self.grayCode(n-1)
            temp = []
            for i in res[::-1]:
                temp.append(i + (2 ** (n-1)))
            res.extend(temp)
        return res

if __name__ == "__main__":
    a = Solution()
    n = 0
    print(a.grayCode(n))
    n = 2
    print(a.grayCode(n))
    n = 0
    print(a.grayCode_1(n))
    n = 2
    print(a.grayCode_1(n))