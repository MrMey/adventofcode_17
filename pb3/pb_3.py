# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:44:05 2017

@author: Mr_Mey
"""


n = 361527

# pb 1
#def steps(n):
#    i = 0
#    number_i = [1]
#    if n == 1:
#        return 0
#    elif n in [2,4,6,8]:
#        return 1
#    elif n == [3,5,7,9]:
#        return 2
#    else:
#        while((2*i + 1)**2 <= n):
#            i += 1
#            number_i.append((2*i+1)**2)
#        print(i)
#        floor = number_i[-2] + 1
#        side = (n - floor) // (2*i)
#        shift = (n - floor) % (2*i)
#        print(side)
#        if shift < i :
#            return 2*i-(shift+1)
#        else:
#            return shift+1
#print(steps(n))

import numpy as np
# pb 2

n = 361527



def compute(n):
    full_r = 10
    r = 1
    center_i = full_r//2
    center_j = full_r//2
    i = center_i
    j = center_j
    big = np.zeros([full_r,full_r])
    big[i,j] = 1
    while True:
        while j-center_j<r:
            big[i,j] = np.sum(big[i-1:i+2,j-1:j+2])
            if big[i,j] >n:
                return(big[i,j])
            j += 1
        while center_i-i<r:
            big[i,j] = np.sum(big[i-1:i+2,j-1:j+2])
            if big[i,j] >n:
                return(big[i,j])
            i -= 1
        while center_j-j<r:
            big[i,j] = np.sum(big[i-1:i+2,j-1:j+2])
            if big[i,j] >n:
                return(big[i,j])
            j -= 1
        while i-center_i<r:
            big[i,j] = np.sum(big[i-1:i+2,j-1:j+2])
            if big[i,j] >n:
                return(big[i,j])
            i += 1
        r += 1

print(compute(n))