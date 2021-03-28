# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:49:28 2020

@author: Harivinay
"""
from random import randint

k = 0.2

t = 0
tmax = 2
dt = 2

A = 4 ## 0
B = 3 ## 1

N = A+B

randomNumberList = [0.800, 0.801, 0.752, 0.661,
                    0.169, 0.956, 0.949, 0.003,
                    0.201, 0.291, 0.615, 0.131,
                    0.241, 0.685, 0.116, 0.241, 0.849]
j = 0
while t < tmax:
    for i in range(N):
        if randomNumberList[j] > A/N:
                A = A-1 
                B = B+1
        else:
            pass
        j+=1
        if randomNumberList[j] > B/N:
            A = A+1
            B = B-1
        else:
            pass
        j+=1
    t = t+dt
    


            
print('A = ',A)
print('B = ',B)
        
        
