# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 20:22:16 2014

@author: Louis
"""
import string

f = open('words')
text = f.read().replace('\n', '')

alpha = string.ascii_letters
for x in alpha:
    if x in text:
        print(x + ': ' + '%1.2f' % (text.count(x)/len(text)))
