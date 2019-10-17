import numpy as np 
import math 

import astropy.constants as c
import astropy.units as u

import matplotlib.pyplot as plt

#m=c.m_e.value #kg
#w=1 #nm
#V=20 #eV
#h=c.hbar.value*u.eV #J*s
#E=np.linspace(0,20, endpoint=False) #eV

m=9.10938356e-31 #kg
w=1 #nm
V=20 #eV
h=1.0545718e-34 #J*s
E=np.linspace(0.01,20, num=1000) #eV

#1ev=1.60*e-19J
x = np.tan(np.sqrt(w**2*m*E/2*h**2)-(np.sqrt(V-E)/E)) #even
y = np.tan(np.sqrt(w**2*m*E/2*h**2))-np.sqrt(E/(V-E)) #odd

y1 = np.tan(np.sqrt(w**2*m*E/2*h**2))
y2 = np.sqrt((V-E)/E)
y3 = -np.sqrt(E/(V-E))

#make approximate estimates of the energies of the 
#first six energy levels of the particle.

plt.plot(E,y1,y2,y3)
