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
    
xa=[0]
ya=[2]
za=[0]
va=31
vxa=31
vya=0
vza=0
dta=0.01

wa=2000*3.1415/3

axa=-(0.0039+0.0058/(1+math.exp((31-35)/5)))*va*31
aya=-9.8
aza=-4.1*10**(-4)*31*w

i=0
while ya[i]>=0:
    xa.append(xa[i]+vxa*dta)
    ya.append(ya[i]+vya*dta)
    za.append(za[i]+vza*dta)
    vxa=vxa+axa*dta
    vya=vya+aya*dta
    vza=vza+aza*dta
    va=(vxa**2+vya**2+vza**2)**0.5
    axa=-(0.0039+0.0058/(1+math.exp((va-35)/5)))*va*vxa
    aza=-4.1*10**(-4)*vxa*wa
    i=i+1
xb=[0]
yb=[3]
zb=[0]
vb=31
vxb=31
vyb=0
vzb=0
dtb=0.01

wb=2000*3.1415/3

axb=-(0.0039+0.0058/(1+math.exp((40-35)/5)))*vb*31
ayb=-9.8
azb=-4.1*10**(-4)*31*wb

i=0
while yb[i]>=0:
    xb.append(xb[i]+vxb*dtb)
    yb.append(yb[i]+vyb*dt)
    zb.append(zb[i]+vzb*dtb)
    vxb=vxb+axb*dtb
    vyb=vyb+ayb*dtb
    vzb=vzb+azb*dtb
    vb=(vxb**2+vyb**2+vzb**2)**0.5
    axb=-(0.0039+0.0058/(1+math.exp((vb-35)/5)))*vb*vxb
    azb=-4.1*10**(-4)*vxb*wb
    i=i+1
    
xc=[0]
yc=[4]
zc=[0]
vc=31
vxc=31
vyc=0
vzc=0
dtc=0.01

wc=2000*3.1415/3

axc=-(0.0039+0.0058/(1+math.exp((45-35)/5)))*vc*31
ayc=-9.8
azc=-4.1*10**(-4)*31*wc

i=0
while yc[i]>=0:
    xc.append(xc[i]+vxc*dtc)
    yc.append(yc[i]+vyc*dtc)
    zc.append(zc[i]+vzc*dtc)
    vxc=vxc+axc*dtc
    vyc=vyc+ayc*dtc
    vzc=vzc+azc*dtc
    vc=(vxc**2+vyc**2+vzc**2)**0.5
    axc=-(0.0039+0.0058/(1+math.exp((vc-35)/5)))*vc*vxc
    azc=-4.1*10**(-4)*vxc*wc
    i=i+1
xd=[0]
yd=[5]
zd=[0]
vd=31
vxd=31
vyd=0
vzd=0
dtd=0.01

wd=2000*3.1415/3

axd=-(0.0039+0.0058/(1+math.exp((31-35)/5)))*vd*31
ayd=-9.8
azd=-4.1*10**(-4)*31*wd

i=0
while yd[i]>=0:
    xd.append(xd[i]+vxd*dtd)
    yd.append(yd[i]+vyd*dtd)
    zd.append(zd[i]+vzd*dtd)
    vxd=vxd+axd*dtd
    vyd=vyd+ayd*dtd
    vzd=vzd+azd*dtd
    vd=(vxd**2+vyd**2+vzd**2)**0.5
    axd=-(0.0039+0.0058/(1+math.exp((vd-35)/5)))*vd*vxd
    azd=-4.1*10**(-4)*vxd*wd
    i=i+1
xe=[0]
ye=[6]
ze=[0]
ve=31
vxe=31
vye=0
vze=0
dte=0.01

we=2000*3.1415/3

axe=-(0.0039+0.0058/(1+math.exp((31-35)/5)))*ve*31
aye=-9.8
aze=-4.1*10**(-4)*31*we

i=0
while ye[i]>=0:
    xe.append(xe[i]+vxe*dte)
    ye.append(ye[i]+vye*dte)
    ze.append(ze[i]+vze*dte)
    vxe=vxe+ax*dte
    vye=vye+aye*dte
    vze=vze+aze*dte
    ve=(vxe**2+vye**2+vze**2)**0.5
    axe=-(0.0039+0.0058/(1+math.exp((ve-35)/5)))*ve*vxe
    aze=-4.1*10**(-4)*vxe*we
    i=i+1
fig = plt.figure(figsize=(10,10))
ax = Axes3D(fig)


plt.xlabel("x(m)")
plt.ylabel("y(m)")
ax.set_zlabel("z(m)")
plt.title("Figure 3  When initial velocity v=31, different initial position Trajectory of battedball")
ax.set_zlim(-1,8)
#plt.ylim(-1.2,1.2)


ax.plot(x, z, y,label="Trajectory (0,0,1)",color="red",linewidth=2)
ax.plot(xa, za, ya,label="Trajectory (0,0,2)",color="orange",linewidth=2)
ax.plot(xb, zb, yb,label="Trajectory (0,0,3)",color="yellow",linewidth=2)
ax.plot(xc, zc, yc,label="Trajectory (0,0,4)",color="green",linewidth=2)
ax.plot(xd, zd, yd,label="Trajectory (0,0,5)",color="blue",linewidth=2)
ax.plot(xe, ze, ye,label="Trajectory (0,0,6)",color="purple",linewidth=2)
ax.scatter(x[0],z[0],y[0],label="Initial Position(0,0,1)",color="red")
ax.scatter(xa[0],za[0],ya[0],label="Initial Position(0,0,2)",color="red")
ax.scatter(xb[0],zb[0],yb[0],label="Initial Position(0,0,3)",color="red")
ax.scatter(xc[0],zc[0],yc[0],label="Initial Position(0,0,4)",color="red")
ax.scatter(xd[0],zd[0],yd[0],label="Initial Position(0,0,5)",color="red")
ax.scatter(xe[0],ze[0],ye[0],label="Initial Position(0,0,6)",color="red")
ax.scatter(x[-1],z[-1],y[-1],label="Final Position (0,0,1)",color="black")
ax.scatter(xa[-1],za[-1],ya[-1],label="Final Position (0,0,2)",color="black")
ax.scatter(xb[-1],zb[-1],yb[-1],label="Final Position (0,0,3)",color="black")
ax.scatter(xc[-1],zc[-1],yc[-1],label="Final Position (0,0,4)",color="black")
ax.scatter(xd[-1],zd[-1],yd[-1],label="Final Position (0,0,5)",color="black")
ax.scatter(xe[-1],ze[-1],ye[-1],label="Final Position (0,0,6)",color="black")
plt.legend()
plt.show()