import matplotlib.pyplot as plt
import numpy as np
import math

x_0=0
y_0=0
Q=135*math.pi/180
v_x_0=1*math.cos(Q)
v_y_0=1*math.sin(Q)
dt=0.001
end_t=100
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
x.append(x_0)
y.append(y_0)
v_x.append(v_x_0)
v_y.append(v_y_0)
t.append(0)

for i in range(int(end_t/dt)):
    x.append(x[i]+v_x[i]*dt)
    y.append(y[i]+v_y[i]*dt)
    v_x.append(v_x[i])
    v_y.append(v_y[i]-1*dt)
    t.append(t[i]+dt)
    #print abs(x[i+1])+abs(y[i+1])
    if  abs(x[i+1])+abs(y[i+1])>1:
        while abs(abs(x[i+1])+abs(y[i+1])-1)>0.00001:
              X=(x[i]+x[i+1])/2
              Y=(y[i]+y[i+1])/2
              a=(2**0.5/2.0)*abs(X)/X
              b=(2**0.5/2.0)*abs(Y)/Y 
              v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
              v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              #v_y[i+1]=-((2.0*a**3-2.0*a)/b)*v_x[i+1]-(2*a**2-1)*v_y[i+1]
              if abs(X)+abs(Y)>1:
                 x[i+1]=X
                 y[i+1]=Y
                 continue
              else:
                 x[i]=X
                 y[i]=Y
                 continue
        #if abs(abs(X)+abs(Y)-1)<0.1:
          # break
x_1=[-1]
y_1=[0]
x_2=[-1]
y_2=[0]
dx=0.1
for j in range(20):
    x_1.append(x_1[j]+dx)
    y_1.append(1-abs(x_1[j+1]))
    x_2.append(x_1[j]+dx)
    y_2.append(-(1-abs(x_1[j+1])))

plt.figure(figsize=(12,12))
plt.plot(x,y,'-' ,label='orbit',color="purple")
plt.plot(x_1,y_1,'-',label='bianary',color="b")
plt.plot(x_2,y_2,'-',color="b")
plt.title(u'Figure 7 square in gravity field $\Theta=135°$',fontsize=18)
plt.xlabel(u'x',fontsize=18)
plt.ylabel(u'y',fontsize=18)
plt.legend(fontsize=14,loc='best')
plt.show()