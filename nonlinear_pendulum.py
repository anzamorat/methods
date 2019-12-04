import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"Non-linear Pendulum"

l=0.1 #Length of pendulum arm in meters 
g=9.81 #Acceleration due to gravity
s_theta=179 #Starting theta in degrees
s_omega=0 #Initial omega

#Array of initial theta and omega
r=np.array([s_theta,s_omega]) #r fully depends on theta and omega

def f(r,t):
    """Return an NxN array consisting of final thetas and final omegas respectively."""

    theta=r[0] 
    omega=r[1]
    f_theta=omega
    f_omega=-(g/l)*np.sin((theta))
    return np.array([f_theta,f_omega])

"RUNGE-KUTTA"

#Defining variables
a=0.0 #Start time
b=100.0 #End time
N=1e4 #Total amount of steps
h=(b-a)/N #Single step size of 1e-2

t_points=np.arange(a,b,h) #Range of time points
theta_points=[] #Empty list to fill for theta_points

#For loop
for t in t_points:

    theta_points.append(r[0]) #Appends theta values
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)

    r = r + (k1+2*k2+2*k3+k4)/6 #Sums over

#Plot displaying theta points vs time points
plt.plot(t_points,theta_points, c='m', lw='3')
plt.title('An epic non-linear pendulum',fontsize=15)

#Zoom in to show detail
plt.xlim([0,4]) #Limit x-axis
plt.show() #Displays plot

"Animation of Pendulum"

#Make figure
fig = plt.figure(figsize=(5,5)) #Size of figure adjustment
fig.suptitle('An epic non-linear pendulum', fontsize=15, fontweight='bold') #Alterted font style
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2)) #Adjusted limits on both axes

#Adds patch
bob = plt.Circle((0,0), radius=0.07, fc='m') #Circle representing bob of pendulum

#Conditions to begin
def init():
    bob.center = (0, 0)
    ax.add_patch(bob)
    return bob,

#Motion of pendulum with derived positions
def animate(i):
    x_position = l*np.cos(theta_points[i]-(np.pi/2)) 
    y_position = l*np.sin(theta_points[i]-(np.pi/2)) 
    bob.center = (x_position, y_position)
    return bob,

#Executes the animation with initial boundaries
ani = animation.FuncAnimation(fig, animate,
init_func=init, frames=360, interval=20, blit=True)

#Saves creation
ani.save('pretty_pendulum.mp4')