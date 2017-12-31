#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:21:56 2017

@author: apple
"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def density(t_end):

    x = list(np.linspace(-100,100,101))
    d = list(np.zeros(50)) + list(np.ones(1)) + list(np.zeros(50))
    d1 = deepcopy(d)

    for i in range(t_end):
        for j in range(101):
            if j==0 or j==100:
                pass
            else:
                d[j] = 0.5* (d1[j+1] + d1[j-1])
        d1 = deepcopy(d)

    for i in range(101):
        if i==0 or i==100:
            pass
        else:
            if d[i]==0:
                d[i] = 0.5*(d1[i+1] + d1[i-1])
    return x, d

x1, d1 = density(50)[0], density(50)[1]
x2, d2 = density(100)[0], density(100)[1]
x3, d3 = density(1000)[0], density(1000)[1]
x4, d4 = density(2000)[0], density(2000)[1]
x5, d5 = density(5000)[0], density(5000)[1]

fig = plt.figure(figsize=[8,6])   
plt.plot(x1,d1,label='steps=50')
plt.plot(x2,d2,label='steps=100')
plt.plot(x3,d3,label='steps=1000')
plt.plot(x4,d4,label='steps=2000')
plt.plot(x5,d5,label='steps=5000')

plt.xlabel('x')
plt.ylabel('probability density')
plt.title('1 dimension when p=0.5, diffusion plot')
plt.xlim(-100,100)
plt.legend()

plt.show()

        
    