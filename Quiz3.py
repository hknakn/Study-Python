# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:53:49 2018

@author: cehak
"""

### QUIZ ###

# %%

list1 = [6,2,9,23,167,9,0,31,3123,7,-1700,-500]

count = 0

for each in list1:
    
    if each < count:
        count = each
    else:
        count = count


print(count)