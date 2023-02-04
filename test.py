#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/30 18:50
# @Author  :  oulinyu 
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import torch
from torch.utils.data import sampler
a = [1,5,78,9,68]
print('SequentialSampler')
b = sampler.SequentialSampler(a)
for x in b:
    print(x)
print('BatchSampler')
b = sampler.BatchSampler(a,batch_size=2,drop_last=False)
for x in b:
    print(x)
print('RandomSampler')
b = sampler.RandomSampler(a)
for x in b:
    print(x)

print('SubsetRandomSampler')
b = sampler.SubsetRandomSampler(a)
for x in b:
    print(x)
print('SubsetRandomSampler')
b = sampler.WeightedRandomSampler(a)
for x in b:
    print(x)
