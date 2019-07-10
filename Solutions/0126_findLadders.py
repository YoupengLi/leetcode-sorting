# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 14:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0126_findLadders.py
# @Software: PyCharm

'''
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest
transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''

import string
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
        # By BFS,
        # find minimum distance for each word
        # from endWord to beginWord
        # and store distance to dict_word_to_distance

        # By DFS,
        # find res based on
        # "dict_word_to_distance[next_word] - dict_word_to_distance[current_word] == -1"
        # and store res to res_list

        dic = set(wordList)
        dic.add(beginWord)

        dict_word_to_distance = {}
        self.bfs(dict_word_to_distance, endWord, dic)

        res_list = []
        res = [beginWord]
        self.dfs(res, res_list, dict_word_to_distance, beginWord, endWord, dic)
        return res_list

    def dfs(self, res, res_list, dict_word_to_distance, beginWord, endWord, dic):

        current_word = beginWord

        if current_word == endWord:
            res_list.append(list(res))
            return

        next_word_list = self.get_next_word_list(current_word, dic)
        for next_word in next_word_list:

            if dict_word_to_distance[next_word] - dict_word_to_distance[current_word] == -1:
                res.append(next_word)

                new_start = next_word
                self.dfs(res, res_list, dict_word_to_distance, new_start, endWord, dic)

                res.pop()

    def bfs(self, dict_word_to_distance, beginWord, dic):
        dict_word_to_distance[beginWord] = 1
        queue = [beginWord]
        while True:
            if len(queue) == 0: return
            current_word = queue.pop(0)
            next_word_list = self.get_next_word_list(current_word, dic)
            for next_word in next_word_list:
                if next_word not in dict_word_to_distance:
                    dict_word_to_distance[next_word] = dict_word_to_distance[current_word] + 1
                    queue.append(next_word)

    def get_next_word_list(self, current_word, dic):
        next_word_list = []
        for i, old_char in enumerate(current_word):
            left = current_word[:i]
            right = current_word[i + 1:]
            for new_char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + new_char + right
                if (new_char != old_char) and (next_word in dic):
                    next_word_list.append(next_word)
        return next_word_list

    def findLadders_1(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
        if endWord not in wordList or not endWord or not beginWord:
            return []
        wordList = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        parents = defaultdict(set)
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction *= -1
            next_foward = set()
            wordList -= forward
            for word in forward:
                for i in range(len(word)):
                    first, second = word[:i], word[i + 1:]
                    for ch in string.ascii_lowercase:
                        combined_word = first + ch + second
                        if combined_word in wordList:
                            next_foward.add(combined_word)
                            if direction == 1:
                                parents[combined_word].add(word)
                            else:
                                parents[word].add(combined_word)
            if next_foward & backward:
                self.res = []
                path = [endWord]
                self.dfs_1(parents, endWord, beginWord, path)
                return self.res
            forward = next_foward
        return []

    def dfs_1(self, parents: 'dict{set}', cur_w: 'str', beginWord: 'str', path: 'List[str]') -> 'None':
        if cur_w == beginWord:
            self.res.append(path[::-1])
            return
        for eword in parents[cur_w]:
            path.append(eword)
            self.dfs_1(parents, eword, beginWord, path)
            path.pop()

if __name__  == "__main__":
    a = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(a.findLadders(beginWord, endWord, wordList))
    print(a.findLadders_1(beginWord, endWord, wordList))
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(a.findLadders(beginWord, endWord, wordList))
    print(a.findLadders_1(beginWord, endWord, wordList))