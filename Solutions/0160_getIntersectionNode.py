# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 10:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0160_getIntersectionNode.py
# @Software: PyCharm

'''
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A:        a1 -> a2 -------
                         |
                         V
                        c1 -> c2 -> c3
                         ^
                         |
B: b1 -> b2 -> b3 -------
begin to intersect at node c1.

Example 1:
A:        4 -> 1 ---------
                         |
                         V
                         8 -> 4 -> 5
                         ^
                         |
B:  5 -> 0 -> 1 ---------
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
A:   0 -> 9 -> 1 ---------
                         |
                         V
                         2 -> 4
                         ^
                         |
B:            3 ---------
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
A:   2 -> 6 -> 4

B:        1 -> 5

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length1 = self.GetLength(headA)
        length2 = self.GetLength(headB)
        if length1 <= 0 or length2 <= 0:
            return None

        if length1 > length2:
            headLong = headA
            headShort = headB
        else:
            headLong = headB
            headShort = headA
        diff = abs(length1 - length2)
        for i in range(diff):
            headLong = headLong.next

        while headLong:
            if headLong is headShort:
                return headLong
            else:
                headLong = headLong.next
                headShort = headShort.next
        return None

    def GetLength(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def getIntersectionNode_1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        S = set()
        while headA:
            S.add(headA)
            headA = headA.next

        while headB:
            if headB in S:
                return headB
            headB = headB.next

        return None

if __name__ == "__main__":
    a = Solution()
    l1 = ListNode(4)
    l2 = ListNode(1)
    l3 = ListNode(8)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(5)
    l7 = ListNode(0)
    l8 = ListNode(1)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l6.next = l7
    l7.next = l8
    l8.next = l3
    print(a.getIntersectionNode(l1, l6).val)
    print(a.getIntersectionNode_1(l1, l6).val)

    l11 = ListNode(0)
    l12 = ListNode(9)
    l13 = ListNode(1)
    l14 = ListNode(2)
    l15 = ListNode(4)
    l16 = ListNode(3)
    l11.next = l12
    l12.next = l13
    l13.next = l14
    l14.next = l15
    l16.next = l14
    print(a.getIntersectionNode(l11, l16).val)
    print(a.getIntersectionNode_1(l11, l16).val)

    l21 = ListNode(2)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l24 = ListNode(1)
    l25 = ListNode(5)
    l21.next = l22
    l22.next = l23
    l24.next = l25
    res = a.getIntersectionNode(l21, l24)
    res = a.getIntersectionNode_1(l21, l24)