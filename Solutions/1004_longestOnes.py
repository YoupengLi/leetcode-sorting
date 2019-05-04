# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 12:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1004_longestOnes.py
# @Software: PyCharm

'''
1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
'''

class Solution:
    def longestOnes(self, A: 'list[int]', K: 'int') -> 'int':
        if not A:
            return 0
        if len(A) <= K:
            return len(A)
        # 建立hash表，键为0第几次出现，值为出现在列表A中的index
        hash = {}
        count_0 = 0
        for i in range(len(A)):
            if A[i] == 0:
                count_0 += 1
                hash[count_0] = i
            else:
                continue
        if count_0 <= K:
            return len(A)
        # 初值赋为hash表键K+1的值，即0第K+1次出现的索引
        max_val = hash[K + 1]
        # 中间运行到count_0-K-1次结束
        for i in range(1, count_0 - K):
            val = hash[K + i + 1] - hash[i] - 1
            if val > max_val:
                max_val = val
            else:
                continue
        # 预留最后一次
        last_val = len(A) - 1 - hash[count_0 - K]
        max_val = max(max_val, last_val)
        return max_val

if __name__ == "__main__":
    a = Solution()
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    print(a.longestOnes(A, K))
    A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    print(a.longestOnes(A, K))
    A = [0, 0, 1, 1, 1, 0, 0, 0]
    K = 0
    print(a.longestOnes(A, K))