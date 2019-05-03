# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 0017 21:36
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0030_findSubstring.py
# @Software: PyCharm

'''
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

import collections
from itertools import product, combinations, permutations
from functools import lru_cache
class Solution:
    def findSubstring(self, s: 'str', words: 'List[str]') -> 'List[int]':
        res = []
        if words == [] or s == "":
                return res
        n = len(words[0])
        n_total = n * len(words)
        for i in list(set(words)):
            if i in s:
                continue
            else:
                return res
        for i in list(set(words)):
            ind = 0
            while True:
                index = s.find(i, ind)
                ind = index + 1
                if index != -1 and (index + n_total) <= len(s):
                    words_1 = words[:]
                    flag = True
                    for j in range(len(words)):
                        temp = s[index + j * n: index + (j+1) * n]
                        if temp in words_1:
                            words_1.remove(temp)
                        else:
                            flag = False
                            break
                    if flag and index not in res:
                        res.append(index)
                else:
                    break
        return res

    def findSubstring_1(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if not words:
            return []
        n = len(words[0])
        if n == 0:
            return [i for i in range(len(s) + 1)]
        seqLen = len(words) * n
        cnt = collections.Counter(words)
        dct = {w: cnt[w] for w in set(words)}
        windows = [dict(dct) for _ in range(n)]
        results = []
        for i in range(len(s)):
            wnd = windows[i % n]
            if i < n - 1:
                continue
            addedWord = s[i - n + 1:i + 1]
            if addedWord in wnd:
                wnd[addedWord] -= 1
            if i >= n + seqLen - 1:
                removedWord = s[i - n - seqLen + 1: i - seqLen + 1]
                if removedWord in wnd:
                    wnd[removedWord] += 1
            if all(l == 0 for l in wnd.values()):
                results.append(i - seqLen + 1)
        return results

    def findSubstring_2(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if not words:
            return []
        ctr = collections.Counter(words).most_common()
        # print(ctr)
        seed = 2221997
        MOD = 10 ** 9 + 7
        n = len(s)
        st = [ord(ch) for ch in s]
        l = len(words[0])
        pw = [1]
        h = [0]
        for i in range(n):
            pw += [(pw[-1] * seed) % MOD]
            h += [(h[-1] + pw[i] * st[i]) % MOD]
        dic = {}
        for t, (word, freq) in enumerate(ctr):
            hashval = 0
            for i in range(l):
                hashval = (hashval + pw[i] * ord(word[i])) % MOD
            hashval = hashval * pw[n - l] % MOD
            dic[hashval] = t
        wd = [-1] * (n + 1)
        for i in range(l, n + 1):
            hashval = pw[n - i] * (h[i] - h[i - l]) % MOD
            if hashval in dic:
                wd[i] = dic[hashval]
        ans = []
        # print(wd)
        for start in range(l):
            diff = 0
            cnt = [freq for word, freq in ctr]
            j = start
            for i in range(start, n + 1, l):
                if wd[i] != -1:
                    cnt[wd[i]] -= 1
                    if cnt[wd[i]] == 0:
                        diff += 1
                        # print(i, j, cnt, diff)

                    while cnt[wd[i]] < 0 or wd[j] == -1:
                        if wd[j] != -1:
                            cnt[wd[j]] += 1
                            if cnt[wd[j]] == 1:
                                diff -= 1
                        j += l
                    if diff == len(ctr):
                        if i - j + l == len(words) * l:
                            ans += [j - l]
        return sorted(ans)

    def findSubstring_3(self, s: 'str', words: 'List[str]') -> 'List[int]':

        if s == "":
            return []
        elif len(words) == 0:
            return []
        elif len("".join(words)) > len(s):
            return []
        elif "".join(words) == s:
            return [0]

        @lru_cache(maxsize=len(set(words)))
        def get_indices(word):
            i = s.find(word)
            indices = list()
            while i != -1:
                # print("i: {}".format(i) )
                indices.append(i)
                i = s.find(word, i + 1)
            return indices

        word_length = len(words[0])
        # print(word_length)

        if len(set(words)) != len(words):
            # Potentially buggy
            # Reject input with O(MN) complexity
            ws = list(set(words))
            ns = ["".join(items) for items in permutations(ws, len(ws))]
            presence = [ss in s for ss in ns]
            if not any(presence):
                return []

        def validate_tuple(x):
            xs = list(x)
            xs.sort()
            i = xs[0]
            for j in range(1, len(xs)):
                # print("i: {} xs[j]: {}".format(i, xs[j]) )
                if xs[j] != i + word_length:
                    return None
                i = xs[j]
            return xs[0]

        m = {word: get_indices(word) for word in words}

        for key, val in m.items():
            if val is None or len(val) == 0:
                return []

        pairs = list(product(*[m[word] for word in words]))
        pairs = set([tuple(sorted(p)) for p in pairs])

        start_indices = [validate_tuple(pair) for pair in pairs]

        return [idx for idx in start_indices if idx is not None]

    def findSubstring_4(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return []
        words_map = collections.defaultdict(int)
        i = end = start = 0
        for word in words:
            words_map[word] += 1
        words_need = len(words)
        words_num = len(words)
        wl = len(words[0])
        starts = set()
        curr_map = collections.defaultdict(int)
        while i < wl:
            start = end = i
            words_need = words_num
            while end < len(s) - wl + 1:
                candidate = s[end:end + wl]
                if candidate in words_map:
                    curr_map[candidate] += 1
                    if curr_map[candidate] <= words_map[candidate]:
                        words_need -= 1
                    while curr_map[candidate] > words_map[candidate]:
                        start_word = s[start:start + wl]
                        curr_map[start_word] -= 1
                        if curr_map[start_word] < words_map[start_word]:
                            words_need += 1
                        start += wl
                    if words_need == 0:
                        starts.add(start)
                else:
                    curr_map.clear()
                    words_need = words_num
                    start = end + wl
                end += wl
            curr_map.clear()
            i += 1
        return list(starts)

    def findSubstring_5(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return []
        for i in list(set(words)):
            if i in s:
                continue
            else:
                return []
        words_map = collections.defaultdict(int)
        i = end = start = 0
        for word in words:
            words_map[word] += 1
        words_need = len(words)
        words_num = len(words)
        wl = len(words[0])
        starts = set()
        curr_map = collections.defaultdict(int)
        while i < wl:
            start = end = i
            words_need = words_num
            while end < len(s) - wl + 1:
                candidate = s[end:end + wl]
                if candidate in words_map:
                    curr_map[candidate] += 1
                    if curr_map[candidate] <= words_map[candidate]:
                        words_need -= 1
                    while curr_map[candidate] > words_map[candidate]:
                        start_word = s[start:start + wl]
                        curr_map[start_word] -= 1
                        if curr_map[start_word] < words_map[start_word]:
                            words_need += 1
                        start += wl
                    if words_need == 0:
                        starts.add(start)
                else:
                    curr_map.clear()
                    words_need = words_num
                    start = end + wl
                end += wl
            curr_map.clear()
            i += 1
        return list(starts)

if __name__ == "__main__":
    a = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    res = a.findSubstring_4(s, words)
    print(res)
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    res = a.findSubstring(s, words)
    print(res)
    s = "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababababababababababababababababababababababababababababababababababababababababababab" \
        "ababababab"
    words = ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba",
             "ab","ba"]
    res = a.findSubstring_5(s, words)
    print(res)