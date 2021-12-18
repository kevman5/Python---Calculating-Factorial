# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:20:59 2021

@author: kevmm
"""

import math



def factorial(factor):
        index = 3
        answer = 1
        while index <= factor:
            answer = answer * index
            index = index + 3
        return answer + 1
    
usersNumber = int(input("Enter number here: "))
print(factorial(usersNumber))