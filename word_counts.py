# coding=utf-8
"""
Use Python to read text from a file,
count the frequency of each independent
words and output them into another text
file
"""

import collections

with open('str.txt') as file1:
    str_count = file1.read().split(' ')

print(str_count)
print(collections.Counter(str_count))
print(collections.Counter(str_count)['Solemnity'])


file2 = open('single.txt','w')

single_words = set(collections.Counter(str_count))

print(single_words)

for i in single_words:
    file2.write(i)
    file2.write(' ')

file2.close()
