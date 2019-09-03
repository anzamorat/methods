#!/usr/bin/env python
# coding: utf-8

# A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away. Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, then print out the time in years that the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth and (b) as perceived by a passenger on board the ship. Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.

# In[9]:


import math
v = float(input("Velocity desired:"))
x = int(input("Distance desired:"))

c = 3*10**8
t0 = x/c
print(t0)

ts = (t0*(math.sqrt(1-v**2/c**2)))
print(ts)

