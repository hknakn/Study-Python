# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 07:30:18 2018

@author: cehak
"""

### LAMBDA FUNCTION ###

# %% 

def calculate(x):
    return x*x

result = calculate(3)

# %% Same thing with the code above

result2 = lambda x: x*x
print(result2(3))