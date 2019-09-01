# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 19:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0208_Trie.py
# @Software: PyCharm

'''
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class TrieNode:
    def __init__(self):
        self.flag = False
        self.children = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.flag = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        res, node = self.childSearch(word)
        if res:
            return node.flag
        return False

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False, None
        return True, cur

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.childSearch(prefix)[0]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    #returns true
    print(trie.search("app"))      #returns false
    print(trie.startsWith("app"))  #returns true
    trie.insert("app")
    print(trie.search("app"))      #returns true