# coding=utf-8

import collections
import os

with open('str.txt') as file1:
    str_count = file1.read().split(' ')

print(str_count)
print(collections.Counter(str_count))
