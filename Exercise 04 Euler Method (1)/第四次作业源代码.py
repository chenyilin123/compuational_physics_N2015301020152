import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

v=[]            #velocity
t=[]            #time
a=10            #assign a value to a
b=1             #assign a value to b
det_t=0.001     #time step
v.append(20)     #assign a value to first item of v[]
t.append(0)     #assign a value to first item of t[]
end_time=20      #total time

for i in range(int(end_time/det_t)):
    tmp=v[i]+(a-b*v[i])*det_t           #Euler method
    v.append(tmp)                       #add new value of v to v[]
    t.append(det_t*(i+1))               #add new value of t to t[]
    print(t[-1],v[-1])                  #print the value of v and t on each stap)

plt.figure(figsize=(12,9))              #set the size of corresponding figure
plt.plot(t,v,label="velocity",color="red",linewidth=1.2) #plot the figure and set label and color and linewidth of the figure
plt.xlabel("time")             #set the label of x axis
plt.ylabel("velocity")       #set the label of y axis
plt.title("Velocity-time Figure") #set title
plt.ylim(0,20)               #set the range of y axis
plt.xlim(0,10)                #set the range of x axis
plt.legend()                   #make it to show everything
plt.show()                     #activate