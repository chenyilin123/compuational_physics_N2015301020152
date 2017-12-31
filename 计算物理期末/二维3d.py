#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:41:50 2017

@author: apple
"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def density(t_end):

    x = np.linspace(-50,50,101)
    y = np.linspace(-50,50,101)
    x,y = np.meshgrid(x,y)
    d = np.zeros((101,101))
    d[50][50]=1
    d1 = deepcopy(d)

    for t in range(t_end):
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)

    for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])

    return x,y,d

x,y,z = density(500)[0],density(500)[1],density(500)[2]
# Plot the surface.


fig = plt.figure(figsize=[8,6]) 
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z,cmap=cm.rainbow)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('probability density')
ax.set_title('2 dimensions, Distribution  , steps=500')
fig.colorbar(surf, shrink=0.5, aspect=7)
plt.xlim(-50,50)
plt.ylim(-50,50)


plt.show()
    