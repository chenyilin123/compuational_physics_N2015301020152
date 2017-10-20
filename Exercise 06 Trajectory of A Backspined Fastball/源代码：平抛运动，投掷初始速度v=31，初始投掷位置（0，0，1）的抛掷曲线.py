import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

x=[0]
y=[1]
z=[0]
v=31
vx=31
vy=0
vz=0
dt=0.01

w=2000*3.1415/3

ax=-(0.0039+0.0058/(1+math.exp((31-35)/5)))*v*31
ay=-9.8
az=-4.1*10**(-4)*31*w

i=0
while y[i]>=0:
    x.append(x[i]+vx*dt)
    y.append(y[i]+vy*dt)
    z.append(z[i]+vz*dt)
    vx=vx+ax*dt
    vy=vy+ay*dt
    vz=vz+az*dt
    v=(vx**2+vy**2+vz**2)**0.5
    ax=-(0.0039+0.0058/(1+math.exp((v-35)/5)))*v*vx
    az=-4.1*10**(-4)*vx*w
    i=i+1


fig = plt.figure(figsize=(10,8))
ax = Axes3D(fig)


plt.xlabel("x(m)")
plt.ylabel("y(m)")
ax.set_zlabel("z(m)")
plt.title("Figure 1  When v =31, Trajectory of battedball")
ax.set_zlim(-1,1)
#plt.ylim(-1.2,1.2)


ax.plot(x, z, y,label="trajectory",color="blue",linewidth=2)
ax.scatter(x[0],z[0],y[0],label="initial position",color="red")
ax.scatter(x[-1],z[-1],y[-1],label="final position",color="black")
plt.legend()
plt.show()