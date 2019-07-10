# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 13:11
# @Author  : Youpeng Li
# @Site    : 
# @File    : getLeetcodeIndex.py
# @Software: PyCharm

import json
import requests
from requests.exceptions import RequestException

'''
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
'''


def get_proble_set(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

url = "https://leetcode.com/api/problems/all/"
html = json.loads(get_proble_set(url))
problemset = html["stat_status_pairs"]
problemset = problemset[::-1]
diff = {1: "Easy", 2: "Medium", 3: 'Hard'}

file = open('./leetcode.txt', 'w+')

for i in range(len(problemset)):
    title = problemset[i]["stat"]["question__title_slug"]
    Title = problemset[i]["stat"]["question__title"]
    difficulty = diff[problemset[i]["difficulty"]["level"]]
    pay = problemset[i]["paid_only"]
    if pay:
        url = str(i+1).zfill(4) + ". [" + Title + "](https://leetcode.com/problems/" + title + ") (" + str(difficulty) + ") [locked]  "
    else:
        url = str(i+1).zfill(4) + ". [" + Title + "](https://leetcode.com/problems/" + title + ") (" + str(difficulty) + ")  "
    file.write(url)  # 写入到“leetcode.txt”文件中
    file.write('\n')
    print(url + "\n")

file.close()