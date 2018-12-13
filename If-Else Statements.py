# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:06:38 2018

@author: cehak
"""

### IF-ELSE STATEMENTS ###

# %% 

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 bigger than var2")
elif(var1 == var2):
    print("var1 and var2 are equal")
else:
    print("var1 smaller than var2")
    
# %% Another example
    
list1 = [1,2,3,4,5,6]

value = 3

if value in list1:
    print("Yes, {} value is in the list".format(value))
else:
    print("No, {} value is not in the list".format(value))
    
# %% Another example
    
dic = {"ali": 25, "veli": 35, "ayşe": 45}

keys = dic.keys()

name = "can"

if name in keys:
    print("Yes, {} is in the dictionary".format(name))
else:
    print("No, {} is not in the dictionary".format(name))
    
    
    
    
    
    
    
    
    