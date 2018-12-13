# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 07:57:28 2018

@author: cehak
"""

### DICTIONARY ###

# %% 

dic = {"ali": 32, "veli": 45, "ayşe": 13}

dic["ali"]

type(dic["ali"])

# "Ali", "Veli", "Ayşe" are Keys
# To see keys of the dictionary

dic.keys()

# To see value of the dictionary

dic.values()

# Use dictionary in a function

def deneme():
    
    dictionary = {"ali": 32, "veli": 45, "ayşe": 13}
    return dictionary

dic = deneme()

# Call function

dic["veli"]
