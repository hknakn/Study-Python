# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 07:18:30 2018

@author: cehak
"""

# USER-DEFINED FUNCTIONS

# %%

a = 10
b = 20

def firstFunc(a,b):
    
    """
    This is my first function
    
    parameter:
        
    return:
        
    """
    
    output = (((a+b)*50)/100)*a/b
    
    return output

result = firstFunc(a,b)

# %%

def secondFunc():
    print("This is my second function.")


# %% Calculate perimeter of a circle 
    
    def circlePerimeter(r, pi = 3.14):
    
        perimeter = 2*pi*r
        return perimeter

# %% Calculate weight and height
        
    def weightHeight(weight,height):
        
        total = weight + height
        return total

# %% Calculate weight, height and age
        
    def wghtHghtAge(weight,height,age):
        
        calculation = (weight + height)*age
        return calculation
        
# %% Using of Args. This is optional parameter
        
    def testArgs(weight,height,*args):
        
        print(args)    
        calculate = (weight * height) * args[0]
        
        return calculate
    
    
    
