# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0016 07:47
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0061_rotateRight.py
# @Software: PyCharm

'''
61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not head or k == 0:
            return head
        pAhead = head
        count = 0
        while pAhead:
            count += 1
            pAhead = pAhead.next
        k = k % count
        if k == 0:
            return head
        pAhead = head
        for i in range(k-1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return head
        pBehind = head
        temp = pBehind
        while pAhead.next:
            pAhead = pAhead.next
            temp = pBehind
            pBehind = pBehind.next
        pAhead.next = head
        head = pBehind
        temp.next = None
        return head

if __name__ == "__main__":
    '''
    1 -> 2 -> 3 -> 4 -> 5 -> None
    '''
    a = Solution()
    t1 = ListNode('1')
    t2 = ListNode('2')
    t3 = ListNode('3')
    t4 = ListNode('4')
    t5 = ListNode('5')

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1
    
    a = Solution()
    res = a.rotateRight(head, 1)
    print(res)

    '''
    0 -> 1 -> 2 -> None
    '''
    t11 = ListNode('1')
    t12 = ListNode('2')
    t11.next = t12

    head = t11

    a = Solution()
    res = a.rotateRight(head, 2)
    print(res)

