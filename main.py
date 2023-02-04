#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/31 20:13
# @Author  :  oulinyu 
# @Site    : 
# @File    : main.py
# @Software: PyCharm
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader,sampler
from Config import Config
def train():
    pass
class ChunkSampler(sampler.Sampler):  # 定义一个取样的函数
    """Samples elements sequentially from some offset.
    Arguments:
        num_samples: # of desired datapoints
        start: offset where we should start selecting from
    """
    def __init__(self, num_samples, start=0):
        self.num_samples = num_samples
        self.start = start

    def __iter__(self):
        '''

        Returns: 返回迭代索引

        '''
        return iter(range(self.start, self.start + self.num_samples))

    def __len__(self):
        return self.num_samples

if __name__ == '__main__':
    config = Config()
    train_set = MNIST('./mnist', train=True, download=True, transform=preprocess_img)
    train_data = DataLoader(train_set, batch_size=config.batch_size, sampler=ChunkSampler(config.NUM_TRAIN, 0))
    val_set = MNIST('./mnist', train=True, download=True, transform=preprocess_img)
    val_data = DataLoader(val_set, batch_size=config.batch_size, sampler=ChunkSampler(NUM_VAL, config.NUM_TRAIN))