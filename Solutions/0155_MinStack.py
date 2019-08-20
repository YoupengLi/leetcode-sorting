# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 10:06
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0155_MinStack.py
# @Software: PyCharm

'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.minstack) == 0:
            self.minstack.append(x)
        else:
            self.minstack.append(min(self.minstack[-1], x))
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.minstack) == 0 or len(self.stack) == 0:
            return None
        self.minstack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__  == "__main__":
    a = MinStack()
    a.push(3)
    a.push(4)
    a.push(2)
    print(a.getMin())
    a.push(1)
    print(a.getMin())
    a.pop()
    a.pop()
    print(a.getMin())