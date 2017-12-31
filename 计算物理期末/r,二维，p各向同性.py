#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:36:57 2017

@author: apple
"""
import math, random, pylab

class Location:
    def __init__(self,x,y):  
        self.x=x
        self.y=y
    def move(self,xc,yc):  
        return Location(self.x+xc,self.y+yc)
    def getLocation(self):
        return self.x,self.y
    def getDistance(self,other):  
        ox,oy=other.getLocation()
        xDist=ox-self.x
        yDist=oy-self.y
        return math.sqrt(xDist**2+yDist**2)

class Direction:
    possibleDirection=("S","W","E","N")  
    def __init__(self,direc):  
        if direc in self.possibleDirection:
            self.direc=direc
        else:
            raise ValueError("in direction:__init__")
    def move(self,dist):  
        if self.direc=="S": return (0,-dist)
        if self.direc=="W": return (-dist,0)
        if self.direc=="E": return (dist,0)
        if self.direc=="N": return (0,dist)
        else: raise ValueError("in direction: move")

class Field:
    def __init__(self,drunk,loc):  
        self.drunk=drunk
        self.loc=loc
    def move(self,direc,dist):  
        oldLoc=self.loc
        xc,yc=direc.move(dist)
        self.loc=oldLoc.move(xc,yc)
    def getLocation(self):
        return self.loc
    def getDrunk(self):
        return self.drunk

class Drunk:
    def __init__(self,name):
        self.name=name
    def move(self,field,step=1):
        if field.getDrunk()!=self:
            raise ValueError("No such drunk is found on the field")
        for i in range(step):
            direc=Direction(random.choice(Direction.possibleDirection))
            field.move(direc,1)

def performTrial(step,f):
    startLoc=f.getLocation()
    distances=[0]
    for t in range(1,step+1):
        f.getDrunk().move(f)
        newLoc=f.getLocation()
        distance=newLoc.getDistance(startLoc)
        distances.append(distance)
    return distances

drunk=Drunk("p=0.25 in four directions, r of 5000 walkers")
for i in range(3):
    f=Field(drunk,Location(0,0))
    distances=performTrial(500,f)
    pylab.plot(distances)
pylab.title("p=0.25 in four directions, random walk in two dimensions")
pylab.xlabel("step number(=Time)")
pylab.ylabel("r")
pylab.show()