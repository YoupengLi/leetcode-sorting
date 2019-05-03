# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 0011 20:36
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0023_mergeKLists.py
# @Software: PyCharm

'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: 'list[ListNode]') -> 'ListNode':
        n = len(lists)
        if n <= 0:
            return []
        else:
            interval = 1
            while interval < n:
                for i in range(0, n - interval, interval * 2):
                    lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
                interval *= 2
            return lists[0]

    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:

            if l1.val < l2.val:
                newlist = l1
                l1 = l1.next
            else:
                newlist = l2
                l2 = l2.next
            h = newlist
            while l1 and l2:
                if l1.val <= l2.val:
                    h.next = l1
                    h = h.next
                    l1 = l1.next
                else:
                    h.next = l2
                    h = h.next
                    l2 = l2.next

            while l1:
                h.next = l1
                l1 = l1.next
                h = h.next
            while l2:
                h.next = l2
                l2 = l2.next
                h = h.next
        return newlist

    def mergeKLists_1(self, lists: 'List[ListNode]') -> 'ListNode':
        nums, dumpy = [], ListNode(0)
        p = dumpy
        for l in lists:
            while l:
                nums.append(l)
                l = l.next
        for i in sorted(nums, key=lambda l: l.val):
            p.next = i
            p = p.next
        return dumpy.next

if __name__ == "__main__":
    '''
    list1: 1 -> 4 -> 5  
    list2: 1 -> 3 -> 4  
    list3: 2 -> 6
    '''
    t1 = ListNode(1)
    t2 = ListNode(4)
    t3 = ListNode(5)
    t1.next = t2
    t2.next = t3
    l1 = t1

    t4 = ListNode(1)
    t5 = ListNode(3)
    t6 = ListNode(4)
    t4.next = t5
    t5.next = t6
    l2 = t4

    t7 = ListNode(2)
    t8 = ListNode(6)
    t7.next = t8
    l3 = t7

    lists = []
    lists.append(l1)
    lists.append(l2)
    lists.append(l3)

    a = Solution()
    res = a.mergeKLists(lists)
    print(res)
