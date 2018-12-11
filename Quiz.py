# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:00:50 2018

@author: cehak
"""

### QUIZ ###

# int , age
# string , name
# function
# built-in function , print, type, len, float
# *args , surname
# default parameter , shoe number

age = 10
name = "Hakan"
surname = "Akın"

def quizFunc (age, name, *args, shoeNum = 43):
    
    print("Name: ", name, "Age: ", age, "Shoe Number:" ,shoeNum)
    print(type(name))
    print(float(age))
    
    output = args[0]*age
    
    return output

result = quizFunc(age, name, surname)

print("args[0]*age: ", result)