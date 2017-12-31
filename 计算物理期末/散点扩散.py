import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(n,t,tt):
    y=[]
    a=[]
    b=[]
    for i in range(tt):
        if i<=7*tt/16 or i>=9*tt/16:
           b.append(0)
        else:
           b.append(n)
    c=[0]*tt
    for j in range(tt):
        y.append(c[:])
        if j<=7*tt/16 or j>=9*tt/16:
           a.append(c[:])
        else:
           a.append(b[:])
    for j in range(t):
        for q in range(len(a)):
            for u in range(len(a)):
                if a[q][u]!=0:
                   for i in range(a[q][u]):
                       cc=random.random()
                       a[q][u]=a[q][u]-1
                       if cc<=0.49:
                          if u+1<=len(a)-1:
                             a[q][u+1]=a[q][u+1]+1
                       elif cc<=0.98:
                          if u-1>=0:
                             a[q][u-1]=a[q][u-1]+1
                       elif cc<=0.99:
                          if q-1>=0:
                             a[q-1][u]=a[q-1][u]+1
                       else:
                          if q+1<=len(a)-1:
                             a[q+1][u]=a[q+1][u]+1                           
    return a
fig = plt.figure(figsize=[15,15]) 
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
plt.xlabel('X',fontsize=18)
plt.ylabel('Y',fontsize=18)
tt=128
y=randpath(10,0,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='b')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax2)
plt.xlabel('X',fontsize=18)
plt.ylabel('Y',fontsize=18)
tt=128
y=randpath(10,10,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='b')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax3)
plt.xlabel('X',fontsize=18)
plt.ylabel('Y',fontsize=18)
tt=128
y=randpath(10,50,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='b')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax4)
plt.xlabel('X',fontsize=18)
plt.ylabel('Y',fontsize=18)
tt=128
y=randpath(10,80,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='b')

plt.xlim(0,tt)
plt.ylim(0,tt)
plt.show()