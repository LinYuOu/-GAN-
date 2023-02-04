#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/31 20:19
# @Author  :  oulinyu 
# @Site    : 
# @File    : Config.py
# @Software: PyCharm
class Config:
    def __init__(self):
        super(Config, self).__init__()
        '''
        Python中的super(Net, self).__init__()是指首先找到Net的父类（比如是类NNet），然后把类Net的
        对象self转换为类NNet的对象，然后“被转换”的类NNet对象调用自己的init函数，其实简单理解就是子类把父类
        的__init__()放到自己的__init__()当中，这样子类就有了父类的__init__()的那些东西
        '''
        self.batch_size=128
        self.NUM_TRAIN = 20000  # 训练集采样个数
        self.NUM_VAL = 5000  # 验证集采样个数

