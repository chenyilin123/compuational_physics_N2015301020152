#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:20:29 2017

@author: apple
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(n,tt):
    b=[]
    bb=[]
    bb1=[]
    for i in range(1,2*n):
        b.append(-n+i)
        bb.append(0)
        if i==n:
           bb1.append(n)
        else:
           bb1.append(0)
    for j in range(n):
        x=[]
        x.append(0) 
        for k in range(tt):   
            c=random.random()
            if c<=0.46:
               x.append(x[-1]+1)
            if c>0.46:
               x.append(x[-1]-1)
        ct=b.index(x[-1])
        bb[ct]=bb[ct]+1/100
    if tt==0:
       return b,bb1
    else:
       return b,bb   


fig = plt.figure(figsize=[15,15])      
ax3=plt.subplot(321)
ax4=plt.subplot(322)
ax5=plt.subplot(323)
ax6=plt.subplot(324)
ax7=plt.subplot(325)
ax8=plt.subplot(326)
colors = ['red', 'tan', 'lime','red', 'tan', 'lime']
plt.sca(ax3)
plt.title("when p=0.46 & different steps, different x 's Probability density plot") 
plt.xlabel('x',fontsize=18)
plt.ylabel('Probability density',fontsize=18)
a,b=randpath(1000,100)
plt.plot(a,b,color='orange')
plt.sca(ax4)
plt.title("when p=0.46 & different steps, different x 's Probability density plot") 
plt.xlabel('x',fontsize=18)
plt.ylabel('Probability density',fontsize=18)
a,b=randpath(1000,500)
plt.plot(a,b,color='orange')
plt.sca(ax5)
plt.xlabel('x',fontsize=18)
plt.ylabel('Probability density',fontsize=18)
a,b=randpath(1000,1000)
plt.plot(a,b,color='orange')
plt.sca(ax6)
plt.xlabel('x',fontsize=18)
plt.ylabel('Probability density',fontsize=18)
a,b=randpath(1000,2000)
plt.plot(a,b,color='orange')
plt.sca(ax7)
plt.xlabel('x',fontsize=18)
plt.ylabel('Probability density',fontsize=18)
a,b=randpath(1000,4000)
plt.plot(a,b,color='orange')
plt.sca(ax8)

plt.xlabel('x',fontsize=18)
plt.ylabel('Probability density',fontsize=18)
a,b=randpath(1000,8000)
plt.plot(a,b,color='orange')
plt.legend(loc='upper right')
plt.show()
"""
for k in range(len(b)):
    plt.scatter([b[k],],[c[k],],3,color='blue')
"""