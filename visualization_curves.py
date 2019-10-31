#!/usr/bin/env python
# coding: utf-8

# # Visual Plots

# ### step 1.

# In[14]:


import math
import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0,2*np.pi , num =200)

x = 2*np.cos(th)+np.cos(2*th)
y = 2*np.sin(th)-np.sin(2*th)

plt.title('Deltoid Curve',fontsize=15)
plt.plot(x,y, 'r>')
plt.show()


# ### step 2.

# In[7]:


def f(theta):
    return th**2

th = np.linspace(0,10*np.pi, num = 200)
r = f(th)
r.size #size


# In[8]:


x2 = r*np.cos(th)
y2 = r*np.sin(th)

plt.title('Spiral',fontsize=15)
plt.plot(x2,y2, 'm+')
plt.show()


# ### step 3.

# "Fey's function"

# In[12]:


th = np.linspace(0,24*np.pi , num=5000)
r = (np.exp(np.cos(th)-2*np.cos(4*th)+np.sin(th/12)**5))
print(r)


# In[13]:


x3 = r*np.cos(th)
y3 = r*np.sin(th)


plt.title('Scissors',fontsize=15)
plt.plot(x3,y3, 'gx')
plt.show()


# ## subplots 

# <b> vertically

# In[21]:


plt.figure(figsize = (3,6)) 
plt.subplot(3,1,1)
plt.plot(x,y,'m')

plt.subplot(3,1,2)
plt.plot(x2,y2, 'r:')

plt.subplot(3,1,3)
plt.plot(x3,y3, 'y-')
plt.show()


# <b> horizontally

# In[24]:


plt.figure(figsize = (25,6)) 
plt.subplot(1,3,1)
plt.plot(x,y, 'k^')

plt.subplot(1,3,2)
plt.plot(x2,y2, 'b.')

plt.subplot(1,3,3)
plt.plot(x3,y3, 'v')
plt.show()

