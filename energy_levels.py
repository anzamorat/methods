import numpy as np 

import astropy.constants as c
import astropy.units as u

import matplotlib.pyplot as plt

"Energy levels in a square potential well"

#Constants
m=c.m_e             #mass weighted in kilograms
w=1.0*u.nm          #width measured in nanometers
V=20*u.eV           #voltage measured in electroVolts
h=c.hbar            #Plancks constant divided by 2pi measured in J*s
E=np.linspace(0.0,20, num=100)*u.eV #Energy measured in eV

values=((w**2*m*E/(2*c.hbar**2)).decompose()).value 
y1 = np.tan(np.sqrt(values))    #tangent
y2 = np.sqrt((V-E)/E)           #even energy levels
y3 = -1*np.sqrt(E/(V-E))        #odd energy levels

def tan_y1(E):
    """Return new values of tangent utilizing adequate equation"""
    E=E*u.eV
    values=((w**2*m*E/(2*c.hbar**2)).decompose()).value #.value takes units away
    new=np.tan(np.sqrt(values))                         #Final equation 
    return new

def even_y2(E):
    V=20
    return np.sqrt((V-E)/E)

def odd_y3(E):
    V=20
    return -1*np.sqrt(E/(V-E))

#Difference of even function from tangent
def tan_even(x):
    return tan_y1(x) - even_y2(x)

#Difference of odd function from tangent
def tan_odd(x):
    return tan_y1(x) - odd_y3(x)

#All respective plots
plt.plot(E,y1,c='r', label='tan') 
plt.plot(E,y2,c='g', label='even')
plt.plot(E,y3,c='b', label='odd')
plt.title('Sq. Quantum Potential-Well',fontsize=15)
plt.xlabel('E expressed in eV', fontsize=13)
plt.ylabel('Respective Quantities', fontsize=13)
plt.ylim([-10,10]) #limit on the y (zooms in)
plt.legend(loc='lower right')
plt.show()

"Binary Method (root finding algorithm)"

tol = 1e-10 #tolerable error

def bisection(f,x1,x2,N):
    '''
    Approximate solution of f(x)=0 on interval [x1,x2] by bisection method...

    Parameters
    ----------
    f: function desired (tan_even or tan_odd)
    x1,x2: interval in which solution must be searched
    N: number of iterations

    Others
    ----------
    x3: midpoint 
    final_x3: final midpoint calculated

    '''

    if f(x1)*f(x2) >= 0:
        print("Bisection method fails")
        return None

    xn = x1
    xp = x2

    #For loop
    for i in range(1,N+1):

        x3 = (x1+x2)/2   #midpoint
        final_x3 = f(x3)   #final midpoint

        if f(x1)*final_x3 < 0:
            x1 = x1
            x2 = x3

        elif f(x2)*final_x3 < 0:
            x1 = x3
            x2 = x2

        elif final_x3 == 0:
            print("Exact solution found")
            return x3

        else:
            print("Bisection method fails")
            return None

    return (x1+x3)/2

bisection(tan_odd,1,2,100)
bisection(tan_even,2,3,100)