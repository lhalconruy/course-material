# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:26:13 2014

@author: Louis
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(len(alphabet)):
    for j in range(i, len(alphabet)):
        if i != j:
            print(alphabet[i]+alphabet[j])
