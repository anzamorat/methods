#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import astropy.constants as c
import astropy.units as u

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[50]:


E0 = c.eps0.value
r = 0.01
q1 = 1
q2 = -1


# In[51]:


def potential(q,r):
    phi=(1/(4*np.pi*e0)*q/r)
    return phi


# In[52]:


N = 100
pot = np.zeros([N,N])
x = np.linspace(0,1, num=N)
y = x

xp = [0.45,0.55]
yp = [0.50,0.50]

for i in range(N):
    for j in range(N):
        x_local = x[j]
        y_local = y[i]
        R1 = np.sqrt((x_local-xp[0])**2+(y_local-yp[0])**2)
        R2 = np.sqrt((x_local-xp[1])**2+(y_local-yp[1])**2)
        
        pot[i][j]= (1/(4*np.pi*E0)*(q1/R1))+(1/(4*np.pi*E0)*(q2/R2))
        
print(R1,R2)


# # potential plot

# In[53]:


map=plt.imshow(pot)
map.set_cmap("viridis")
plt.title("lovely charges", fontsize=15)
plt.show()


# # central difference 
# (f(x+h/2)-f(x-h/2))/h
# 
# # use this format to calculate derivatives
# f(x+h)-f(x))/h
# 
# 
# f(y+h)-f(y))/h

# In[54]:


#provides electric field

h = 1/N

E_x = np.zeros([N,N])
E_y = np.zeros([N,N])

for i in range(1,N-1):
    for j in range(1,N-1):

        partialx = (pot[i+1][j] - pot[i-1][j])/(2*h) #central difference for x components
        partialy = (pot[i][j+1] - pot[i][j-1])/(2*h) #central difference for y components
        E_x[i][j] = partialx
        E_y[i][j] = partialy


# In[64]:


scale=1e-13 #zoom in/out

fig,ax=plt.subplots()

for i in range(1,N,10):
    for j in range(1,N,10):
        plt.arrow(x[j],y[i],scale*E_x[i][j],scale*E_y[i][j], color='b')
        
ax.set_title('Electric Field :)', fontsize=15)
ax.set_ylim([0,1])
ax.set_xlim([0,1])
plt.show()


# In[15]:


#draw electric field
#draw potential
#side-by-side plots

