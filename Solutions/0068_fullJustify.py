# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 17:49
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0068_fullJustify.py
# @Software: PyCharm

'''
68. Text Justification

Given an array of words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

import math
class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        res = []
        temp = []
        temp_len = 0
        for i in range(len(words)):
            if temp_len + len(words[i]) <= maxWidth:
                temp.append(words[i])
                temp_len += (len(words[i]) + 1)
            else:
                if len(temp) == 1:
                    temp += (maxWidth - len(temp[0])) * " "
                    temp = "".join(temp)
                    res.append(temp)
                else:
                    num_b = maxWidth - len("".join(temp))
                    a = num_b // (len(temp) - 1)
                    b = num_b % (len(temp) - 1)
                    if b:
                        for j in range(b):
                            temp[j] += " "
                    temp = (" " * a).join(temp)
                    res.append(temp)
                temp = []
                temp.append(words[i])
                temp_len = len(words[i]) + 1
            if i == len(words)-1:
                if len(temp) == 1:
                    temp += (maxWidth - len(temp[0])) * " "
                    temp = "".join(temp)
                    res.append(temp)
                else:
                    temp = " ".join(temp) + (maxWidth - len(" ".join(temp))) * " "
                    res.append(temp)
        return res

    def fullJustify_1(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        text = []
        current_list = []
        current_line = ''
        while words:
            if len(current_line) + len(words[0]) + 1 <= maxWidth:
                current_list.append(words.pop(0))
                current_line += current_list[-1] + ' '
            elif len(current_line) + len(words[0]) == maxWidth:
                current_list.append(words.pop(0))
                current_line += current_list[-1] + ' '
            else:
                text.append(self.reorganize(current_list, maxWidth))
                current_list = []
                current_line = ''

        # the last line remaining to be processed
        word_len = sum([len(c) for c in current_list])
        white_len = len(current_list) - 1
        last_line = self.reorganize(current_list, word_len + white_len)
        last_line += ' ' * (maxWidth - len(last_line))
        text.append(last_line)
        return text

    def reorganize(self, current_list, maxWidth):
        word_num = len(current_list)
        res_line = ''
        if word_num == 1:
            white_space = maxWidth - len(current_list[0])
            res_line += current_list[0] + ' ' * white_space
            return res_line
        else:
            slot_num = word_num - 1
            white_space = maxWidth - sum([len(c) for c in current_list])
            avg = white_space // slot_num
            resual = white_space % slot_num
            scope = 1
            white_space_list = [' ' * avg] * slot_num
            while resual > 0:
                avg = resual // (slot_num - scope)
                resual = resual % (slot_num - scope)
                for i in range(0, slot_num - scope):
                    white_space_list[i] += ' ' * avg
                scope += 1
            for i in range(slot_num):
                res_line += current_list[i] + white_space_list[i]
            res_line += current_list[-1]
            return res_line

if __name__ == "__main__":
    a = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    res = a.fullJustify(words, maxWidth)
    print(res)
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    res = a.fullJustify(words, maxWidth)
    print(res)
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    res = a.fullJustify(words, maxWidth)
    print(res)
    words = ["Listen", "to", "many,", "speak", "to", "a", "few."]
    maxWidth = 6
    res = a.fullJustify(words, maxWidth)
    print(res)
    words = ["ask", "not", "what", "your", "country", "can", "do", "for", "you",
             "ask", "what", "you", "can", "do", "for", "your", "country"]
    maxWidth = 16
    res = a.fullJustify(words, maxWidth)
    print(res)
    words = ["a", "b", "c", "d", "e"]
    maxWidth = 3
    res = a.fullJustify(words, maxWidth)
    print(res)