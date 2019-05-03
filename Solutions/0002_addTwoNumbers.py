# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 0016 下午 2:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0002_addTwoNumbers.py
# @Software: PyCharm

'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

The pseudocode is as following:
<1> Initialize current node to dummy head of the returning list.
<2> Initialize carry to 0.
<3> Initialize p and q to head of l1 and l2 respectively.
<4> Loop through lists l1 and l2 until you reach both ends.
    Set x to node p's value. If p has reached the end of l1, set to 0.
    Set y to node q's value. If q has reached the end of l2, set to 0.
    Set sum = x + y + carry.
    Update carry = sum / 10.
    Create a new node with the digit value of (sum mod 10) and set it to current node's next,
        then advance current node to next.
    Advance both p and q.
<5> Check if carry=1, if so append a new node with digit 11 to the returning list.
<6> Return dummy head's next node.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        carry = 0
        head = l1
        p1 = None  # p1储存l1的上一个节点

        while l1 or l2 or carry != 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            val = sum % 10
            carry = sum // 10
            '''
            if not l1:
                if l2:
                    l1 = ListNode(l2.val)
                else:
                    l1 = ListNode(val)
                p1.next = l1
            '''
            if not l1:
                l1 = ListNode(val)
                p1.next = l1
            l1.val = val
            p1 = l1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head

if __name__ == "__main__":
    p1 = ListNode(2)
    p2 = ListNode(4)
    p3 = ListNode(9)
    p4 = ListNode(1)
    p5 = ListNode(2)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    head1 = p1

    p11 = ListNode(5)
    p12 = ListNode(6)
    p13 = ListNode(4)

    p11.next = p12
    p12.next = p13

    head2 = p11

    a = Solution()
    res = a.addTwoNumbers(head2, head1)
    print(res.val)