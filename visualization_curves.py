#!/usr/bin/env python
# coding: utf-8

# # deltoid curve

# ### step 1.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace

th = np.linspace(0,2*np.pi , num =200)

x = 2*np.cos(th)+np.cos(2*th)
y = 2*np.sin(th)-np.sin(2*th)

print(x)
print(y)

plt.plot(x,y)


# ### step 2.

# In[6]:


def f(theta):
    return th**2

th = np.linspace(0,10*np.pi, num = 200)
r = f(th)
r.size #size


# In[7]:


x2 = r*np.cos(th)
y2 = r*np.sin(th)

plt.plot(x2,y2)


# ### step 3.

# "Fey's function"

# In[8]:


th = np.linspace(0,24*np.pi , num=5000)
r = (np.exp(np.cos(th)-2*np.cos(4*th)+np.sin(th/12)**5))
print(r)


# In[9]:


x3 = r*np.cos(th)
y3 = r*np.sin(th)

plt.plot(x3,y3)


# ## subplots 

# <b> vertically

# In[10]:


plt.figure(figsize = (3,6)) 
plt.subplot(3,1,1)
plt.plot(x,y, color='m')


plt.subplot(3,1,2)
plt.plot(x2,y2, linestyle = ":")

plt.subplot(3,1,3)
plt.plot(x3,y3)


# <b> horizontally

# In[11]:


plt.figure(figsize = (25,6)) 
plt.subplot(1,3,1)
plt.plot(x,y, c='y')


plt.subplot(1,3,2)
plt.plot(x2,y2, linestyle=":", c="k")

plt.subplot(1,3,3)
plt.plot(x3,y3, linestyle="--", c="g")

