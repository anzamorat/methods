import numpy as np 

import math 

import astropy.constants as c
import astropy.units as u

import matplotlib.pyplot as plt

m=c.m_e #kg
w=1.0*u.nm #nm
V=20*u.eV #eV
h=c.hbar #J*s
E=np.linspace(0.0,20, num=100)*u.eV #eV

values=((w**2*m*E/(2*c.hbar**2)).decompose()).value
y1 = np.tan(np.sqrt(values)) #tangent
y2 = np.sqrt((V-E)/E) #even energy levels
y3 = -np.sqrt(E/(V-E)) #odd energy levels

def tan_y1(E):
    E=E*u.eV
    values=((w**2*m*E/(2*c.hbar**2)).decompose()).value
    new=np.tan(np.sqrt(values))
    return new

def even_y2(E):
    V=20
    return np.sqrt((V-E)/E)

def odd_y3(E):
    V=20
    return -1*np.sqrt(E/(V-E))

#difference of even function from tangent
def tan_even(x):
    return tan_y1(x) - even_y2(x)

#difference of odd function from tangent
def tan_odd(x):
    return tan_y1(x) - odd_y3(x)

#PLOT
plt.plot(E,y1,c='r', label='tan')
plt.plot(E,y2,c='g', label='even')
plt.plot(E,y3,c='b', label='odd')
plt.title('Sq. Quantum Potential-Well',fontsize=15)
plt.xlabel('E expressed in eV', fontsize=13)
plt.ylabel('Respective Quantities', fontsize=13)
plt.ylim([-10,10]) #limit on the y (zooms in)
plt.legend(loc='lower right')
plt.show()

#BISECTION
tol = 1e-10

def bisec(x1,x2,func):
    xp=0
    xn=0
    if func(x1) > 0:
        xp=x1
    else:
        xn=x1
    if func(x2) < 0:
        xn=x2
    else:
        xp=x2
    print(xp)
    print(xn)
    while np.abs(xp-xn) > tol:
        x3=(xn+xp)/2 #halfway
        if func(x3) > 0:
            xp=x3
        else:
            xn = x3
return (xn+xp)/2

bisec(2,-1,tan_even)