# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:49:46 2018

@author: cehak
"""

### WHILE LOOP ###

# %%

i = 0

while (i < 4):
    print(i)
    i = i + 1

# %% 
    
list1 = [1,4,6,7,8,21,675,98,2,344,5,312]

const = len(list1)
each = 0
count = 0

while (each < const):
    count = count + list1[each]
    print(count)
    each = each + 1
    