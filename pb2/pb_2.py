# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 17:56:43 2017

@author: Mr_Mey
"""

import numpy as np

# part 1
cnt = 0
input_arr = np.loadtxt('input_pb_2.txt')

for i in range(input_arr.shape[0]):
    min_val = min(input_arr[i,:])
    max_val = max(input_arr[i,:])
    cnt += max_val - min_val
print(int(cnt))

# part 2

cnt = 0

for i in range(input_arr.shape[0]):
    input_arr[i,:] = np.sort(input_arr[i,:])
    
    j = 0
    k = 1
    # hypothèse d'un nombre pair de colonnes
    while (j < input_arr.shape[1]//2) and (input_arr[i,k] % input_arr[i,j] != 0):
        k = k + 1
        if k >= input_arr.shape[1]:
            j += 1
            k = j + 1
    cnt += input_arr[i,k] // input_arr[i,j]
print(int(cnt)) 