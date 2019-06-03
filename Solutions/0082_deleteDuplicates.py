# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 16:24
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0082_deleteDuplicates.py
# @Software: PyCharm

'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        '''
        use a prev var to store previous node's value and update it in every iteration;
        dummy_cur.next is updated when there cur pair is diff;
        in the next iteration, dummy_cur only advances when next pair is different and dummy_cur.next is not None, 
        otherwise set to None.
        '''
        dummy = dummy_cur = ListNode(0)
        prev = head
        cur = head

        while cur:
            if prev is not None and prev == cur.val:
                dummy_cur.next = None
            else:
                if dummy_cur.next:
                    dummy_cur = dummy_cur.next
                dummy_cur.next = cur
            prev = cur.val
            cur = cur.next

        return dummy.next

if __name__ == "__main__":
    '''
    list1: 1->2->3->3->4->4->5
    '''
    a = Solution()
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(3)
    t5 = ListNode(4)
    t6 = ListNode(4)
    t7 = ListNode(5)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    t6.next = t7

    head = t1

    head = a.deleteDuplicates(head)
    print(head)