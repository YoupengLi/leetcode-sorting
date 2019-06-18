# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 22:03
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0092_reverseBetween.py
# @Software: PyCharm

'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        cur, prev = head, dummy

        for _ in range(m-1):
            cur = cur.next
            prev = prev.next

        for _ in range(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

    def reverseBetween_1(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            pre = pre.next
        cur = pre.next
        # reverse the defined part
        node = None
        for _ in range(n - m + 1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        # connect three parts
        pre.next.next = cur
        pre.next = node
        return dummy.next

if __name__ == "__main__":
    '''
    list1: 1->2->3->4->5
    '''
    a = Solution()
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t5 = ListNode(5)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1
    m = 2
    n = 5
    res = a.reverseBetween(head, m, n)
    print(res)