#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import astropy.constants as c
import astropy.units as u

import warnings
warnings.filterwarnings('ignore')

import mpmath as math


# In[2]:


print(c.k_B)
print(c.c)
print(c.hbar)


# ## stefan-boltzmann
# describes the power radiated from a black body in terms of its temperature
#  
# 5.67 x 10 -8 watt per meter squared per kelvin to the fourth (W. m^2. K^4 )

# In[7]:


#total energy per unit area radiated by a black body
W = (c.k_B)**4/(4*np.pi**2*(c.c)**2*(c.hbar)**3)
e = np.e

def f(x):
    z = np.tan(x)
    f = ((z**3)*math.sec(x)**2)/((e**(z)-1))
    return f

a = 0.000001
b = np.pi/2
N = 10**3
d = ((b-a)/N)
s = 0.5*f(a) + 0.5*f(b)
fsum = 0
k = 1


# In[8]:


#adding all the values
for k in range(1,N):
        s += f(a+k*d)


# In[9]:


T = d*(0.5*f(a)+0.5*f(b)+s) #trapezoidal rule to compute integral
print(T) #integral of W

print("Stefan-Boltzmann:", W*T)

