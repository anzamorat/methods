#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

import matplotlib.pyplot as plt

import time 
import timeit #runs it a million times


# <b>Exercise 4.3</b> Derivatives
#     
# <b>part A)</b> Write a program that defines a function f(x) returning the value x(x−1), then calculates the derivative of the function at the point x = 1 using the formula above with δ = 10−2

# In[13]:


#calculating derivatives

def f(x):
    function=x*(x-1)
    return function

delta=1e-2

#location:
x=1

#derivative
dfdx=(f(x+delta)-f(x))/(delta)
print("Derivative: %0.4f" % dfdx)


# <b> part B)</b> Repeat the calculation for δ = 10−4, 10−6, 10−8, 10−10, 10−12, and 10−14. You should see that the accuracy of the calculation initially gets better as δ gets smaller, but then gets worse again. Plot your result as a function of δ . WHY is this?

# In[49]:


DELTAS=np.array([1e-4, 1e-6, 1e-8,1e-10,  1e-12 , 1e-14])

#all derivatives in the above delta values
dfdx=(f(x+DELTAS)-f(x))/(DELTAS)
print(dfdx)

plt.plot(np.log10(DELTAS), dfdx, 'b>') 
#log10 because OG values are tiny
plt.title('Accuracy',fontsize=15)
plt.xlabel('Delta Values', fontsize=13)
plt.xlim([-16,-2])
plt.ylabel('Respective Accuracies', fontsize=13)
plt.show()


# <b>Excercise 4.4</b> Integrals

# <b>part a|</b> hint: value of the integral (area under semicircle) must be pi/2

# In[78]:


#Riemann definition of the integral

start=time.time()
def integral(N):
    if N<0:
        return 0
    
    result=0
    h=2/N #width
    
    for k in range(1,N+1):
        x=-1+h*k
        y=np.sqrt(1-x**2)
        result+=h*y #sums over
        
    end=time.time() 
    return result

print(integral(100))

#N gets more accurate as it increases
#Hence, 100 slices is not enough!

print(f"Program took :{end-start} seconds to run")


# <b>part b

# In[79]:


#Increase the value of N (number of slices)

start=time.time()
def integral(N):
    if N<0:
        return 0
    
    result=0
    h=2/N #width
    
    for k in range(1,N+1):
        x=-1+h*k
        y=np.sqrt(1-x**2)
        result+=h*y #adds over
        
    end=time.time()
    return result
        
print(integral(100000))

print(f"Program took {end-start} seconds to run")

