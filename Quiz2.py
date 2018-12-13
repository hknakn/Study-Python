# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:19:38 2018

@author: cehak
"""

### QUIZ 2 ###

# %% Calculate year to century

year = 17

float(year)   
  
def year2Centruy(year):  
    calc = year / 100
    int(calc)
    cent = calc + 1
    return int(cent)

year2Centruy(year)