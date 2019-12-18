import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import astropy.constants as c 
from scipy import optimize

""" The famous Brachistochrone curve is the path down which a marble will 
fall between two points in the least time without friction (an arc of a cycloid),
what path should a frictionless object follow when travelling between 
two points under gravity alone to minimise its time of travel? """

#step 1. Execute brachistochrone with fixed radius ("dummy model")

"First section of Brachistochrone"

#Initial conditions
xi=0           #Initial x-value
xf=2           #Final x-value

a=1            #Radius of circle (fixed)
N=1e5          #Number of steps
h=(xf-xi)/N    #Size of single step

def model(y,x):
    dxdy=np.sqrt(y/(2.0*a-y))
    return dxdy

x_points=[]    #Empty list to fill values with x-values
x=0
y_points=np.arange(xi,xf,h) #Range of y-values

#For loop for first set of x-points based on y-points including ODE
for y in y_points:
    x_points.append(x)
    x += h*model(y,x)

"Second section of brachistochrone"

x2_points=[]
x2=2*pi

#For loop for second set of x-points to complete "brachistochrone"
for y in y_points:
    x2_points.append(x2)
    x2 += -h*model(y,x)       #Negative sign so it draws it backwards

#Plot over 2pi
plt.title('BRACHI',fontsize=15,fontweight='bold')
plt.xlabel('Position {x}')
plt.ylabel('Position {-y}')
plt.plot(x_points,y_points,c='g',lw='2')
plt.plot(x2_points,y_points,c='g',lw='2')
plt.gca().invert_yaxis()      #Inverts y-axis
plt.show()

#step 2. Given my boundaries: x-final and y-final, what is the radius of my cycloid?

#Acceleration of gravity on Earth
g=c.g0 #m/s^2 {takes away units}

#Input the 2 endpoints {xF,yF}
xF=int(input("Final x-point: "))
yF=int(input("Final y-point: "))

#Implementing Newton-Raphson or secant method: Find a zero of the desired function "model" given a nearby starting point x0 using this method.
def brachi(xF, yF, N):
    
    """
    Returns the path of Brachistochrone curve from origin to (xF, yF)

    a: radius
    xF: final x-coordinate
    yF: final y-coordinate
    yF/xF: final position of marble
    theta: angle 
    final_theta: final rolling angle from desired endpoints
    g: standard acceleration of gravity
    N: total number of steps
    h: single step
    
    """

    #Find 'final_theta' numerically from endpoints (xF,yF)
    
    def function(theta): #Theta may be found with code below
        return yF/xF - (1-np.cos(theta))/(theta-np.sin(theta))
    
    #Compute 'final_theta' numerically with second theta calculated using newton's method
    final_theta = optimize.newton(function, np.pi/2)

    #Radius of the circle generating the cycloid
    a = yF/(1-np.cos(final_theta))
    
    #Evenly-spaced values from initial value to final theta by N points
    theta = np.linspace(0, final_theta, N)
    
    #Parametric solutions in the form of a cycloid:
    x = a*(theta-np.sin(theta))
    y = a*(1-np.cos(theta))
    
    #Traveled time between(0,0) and endpoints {xF,yF}
    t = np.sqrt(a/g)*final_theta
    print('Radii = {:.3f}'.format(a))          #Formatted to 3 significant figures
    print('Time traveled = {:.2f}'.format(t))  #Formatted to 2 significant figures

brachi(xF,yF,N)

#step 3. One loop for everything with markers (bead)

#Feed radius found to model
x0=0 
y0=0
N=10**7                            #Number of steps
h=(xF-x)/N                         #Size of single step

#Function passing differential equation
def model(y,x):
    dxdy=np.sqrt(y/(2.0*a-y))
    return dxdy

y_points=np.arange(y0,2*a,h)
x_points,x2_points=[],[]

#Beginning of second part of x-points where my values will append
x2=2*pi*a 

#For loop
for y in y_points:
    x_points.append(x0)   #First set of points appending to x(0)
    x2_points.append(x2)  #Second set of points appending to x2 which varies based on radii
    x += h*model(y,x)     #Given values passed through the product of model & single step values
    x2 += -h*model(y,x)   #Given values passed through the product of model & single step values

#Plots brachistochrone with markers
plt.scatter(0,0,c='r', label='start')                   #Plots marker (bead) in initial condition 
plt.scatter(xF,yF,c='m', label='endpoint')              #Plots marker on endpoints chosen

plt.plot(x_points,y_points, c='k',lw='3')               #1st section of Brachistochrone
plt.plot(x2_points,y_points,c='k',lw='3')               #2nd section of Brachistochrone 
plt.xlabel('Position {x}')
plt.ylabel('Position {-y}')
plt.gca().invert_yaxis()                                #Invert y-axis 

#Legend details
leg = plt.legend(loc='best', shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.7)

#Displays plot when running on terminal
plt.show()

#step 4. Animation of brachistochrone 
"Animation of Brachistochrone (didn't work but I tried) :("

#Create figure
fig = plt.figure()
ax = plt.axes()
ax.plot(x_points,y_points, c='k')
ax.plot(x2_points,y_points, c='k')
ax.invert_yaxis()                                     #Invert y-axis 

#Adds circle patch of marble
marble = plt.Circle((0,0), radius=0.09, fc='c')

#Initial position 
def init():
    marble.center = (0, 0)
    ax.add_patch(marble)
    return marble,

#Animate function based on {x,y} positions
def animate(i):
    x_position = x_points[i]
    y_position = y_points[i]
    marble.center = (x_position, y_position)
    return marble,

plt.xlabel('Position {x}', fontsize=13)
plt.ylabel('Position {-y}',fontsize=13)

ani = animation.FuncAnimation(fig, animate,
init_func=init, frames=360, interval=20, blit=True)

#Saves creation
ani.save('brachi_baby.mp4')

plt.show() 

