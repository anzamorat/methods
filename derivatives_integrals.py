#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time 
import timeit #runs it a million times


# In[10]:


start=time.time()
end=time.time()
print(end-start)
print(start)
print(end)


# In[11]:


#examples
print(timeit.timeit("5+5/3"))
print(timeit.timeit("5+5/math.sqrt(3)", "import math"))


# In[2]:


import math
import numpy as np

import matplotlib.pyplot as plt


# <b>Exercise 4.3</b> Derivatives
#     
# <b>part A)</b> Write a program that defines a function f(x) returning the value x(x−1), then calculates the derivative of the function at the point x = 1 using the formula above with δ = 10−2

# In[8]:


#calculating derivatives

def f(x):
    function=x*(x-1)
    return function

delta=1e-2

#location:
x=1

#derivative
dfdx=(f(x+delta)-f(x))/(delta)
print("Derivative %0.2f" % dfdx)


# <b> part B)</b> Repeat the calculation for δ = 10−4, 10−6, 10−8, 10−10, 10−12, and 10−14. You should see that the accuracy of the calculation initially gets better as δ gets smaller, but then gets worse again. Plot your result as a function of δ . WHY is this?

# In[60]:


DELTAS=np.array([1e-4, 1e-6, 1e-8,1e-10,  1e-12 , 1e-14])

#all derivatives in the above delta values
dfdx=(f(x+DELTAS)-f(x))/(DELTAS)
print(dfdx)

plt.plot(np.log10(DELTAS), dfdx, 'gd') #log10 because OG values are tiny
plt.title('Accuracy',fontsize=15)
plt.xlabel('Delta Values', fontsize=13)
plt.ylabel('Respective Accuracies', fontsize=13)
plt.show()


# <b>Excercise 4.4</b> Integrals

# In[3]:


#Riemann definition of the integral

def integral(N):
    top=0
    h=2/N
    x=np.linspace(-1,1,100)
    y=np.sum(np.sqrt(1-x**2))
    top= h*y
    return top

print(integral(1000))

#N gets more accurate as it increases

