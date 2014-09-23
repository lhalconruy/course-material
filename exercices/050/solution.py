# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:03:08 2014

@author: Louis
"""

n = 0
for i in range(1000):
    if (i % 3 == 0) | (i % 5 == 0):
        n = n + i
print(n)
