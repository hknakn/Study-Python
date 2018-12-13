# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 07:35:47 2018

@author: cehak
"""

### LIST ###

# %%

list_int = [1,2,3,4,5,6]
type(list_int)

list_str = ["ptesi", "sali", "cars"]
type(list_str)

# %% Print any value of list

value = list_int[1]
print(value)

# %% Print last value of list
last_value = list_int[-1]
print(last_value)

# %% Print selected and excluded values of the list 

list_divide = list_int[0:3]
print(list_divide)

# %% See methods of List

dir(list_int)

# %% See help of selected method

help(list.append)

# %% Add a value to end of the list

list_int.append(7)
print(list_int)

# %% Remove a value of the list

list_int.remove(7)
print(list_int)

# %% Reversing the list

list_int.reverse()
print(list_int)

# %% Sorting the list

list2 = [5,3,9,2,0,7,8,4,1,23]
list2.sort(reverse = True)
print(list2)
