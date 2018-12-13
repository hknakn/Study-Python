# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:34:52 2018

@author: cehak
"""

### FOR LOOP ###

# %%

for each in range(1,12):
    print(each)
    
# %%
    
for each in ("ankara ve istanbul"):
    print(each)
    
# %% Split the words by space
    
for each in "ankara istanbul".split():
    print(each)
    
# %% Summation of the list
    
list1 = [1,3,4,6,7,8,9,212,456,77,89,245]

sum = 0

for each in list1:
    sum = sum + each
    print(sum)