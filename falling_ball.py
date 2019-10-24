#!/usr/bin/env python
# coding: utf-8

# <b>Exercise 2.1:</b> Ball dropped from a tower
# 
# A ball is dropped from a tower of height h with initial velocity zero. Write a program that asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring air resistance. Use your program to calculate the time for a ball dropped from a 100 m high tower.

# In[1]:


import numpy as np 

import math 

import astropy.constants as c
import astropy.units as u


# In[3]:


#formula: 
#h=vt + 0.5gt^2
#v=0, hence becomes-> 0.5gt^2
#but when solving for time becomes
#t=(h*2)/g

h=float(input("Enter the HEIGHT in meters: ")) #m
g=c.g0.decompose().value #m/s^2 (acceleration of gravity on Earth)


# In[10]:


#new formula:
t=math.sqrt(h*2/g)

print("TIME calculated for the ball to touch the ground is: %0.2f" 
                                                  % t,"in seconds")

