# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:42:00 2020

@author: Harivinay
"""

from random import randint

success = 0
attempts = 1000000

for i in range(attempts):
    if randint(0,1)+randint(0,1)+randint(0,1)+randint(0,1)==3:
        success+=1
        
percent = success/attempts

print("Attempts", attempts)
print("Success", success)
print("Precent", percent)