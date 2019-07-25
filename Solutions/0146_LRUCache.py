# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 8:50
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0146_LRUCache.py
# @Software: PyCharm

'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

from collections import deque, OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.order = []
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            self.order.remove(key)
            self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) == self.cap:
            self.cache.pop(self.order[0])
            self.order.pop(0)

        self.order.append(key)
        self.cache[key] = value

class LRUCache_1(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.deque = deque([])
        self.dic = {}
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.deque.remove(key)
        elif len(self.dic) == self.cap:
            v = self.deque.popleft()  # remove the Least Recently Used element
            self.dic.pop(v)
        self.deque.append(key)
        self.dic[key] = value

class LRUCache_2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.order, self.cap = OrderedDict(), capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.order:
            return -1
        self.order.move_to_end(key)
        return self.order[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.order:
            del self.order[key]
        elif len(self.order) == self.cap:
            self.order.popitem(False)
        self.order[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    cache = LRUCache_1(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    cache = LRUCache_2(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))