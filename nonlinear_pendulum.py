import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"NONLINEAR PENDULUM"

l=0.1 #u.m
g=9.81 #c.g0 
s_theta=179 #degrees
s_omega=0

#PERIOD=2pi/omega
#OMEGA=2pi/T

def f(r,t):
    theta=r[0] 
    omega=r[1]
    f_theta=omega
    f_omega=-(g/l)*np.sin(np.radians(theta))
    return np.array([f_theta,f_omega])

"RUNGE-KUTTA"

a=0.0 #start tikme
b=100.0 #end time
N=1e4 #total amount of steps
h=(b-a)/N #single step size of 1e-2

r=np.array([s_theta,s_omega])

t_points=np.arange(a,b,h) 
theta_points=[]

for t in t_points:
    theta_points.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)

    #sums over
    r = r + (k1+2*k2+2*k3+k4)/6

plt.plot(t_points,theta_points, c='r', lw='3')
plt.title('An epic non-linear pendulum',fontsize=15)
plt.xlim([0,50])
plt.show()

"ANIMATION"

fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

bob = plt.Circle((0,0), radius=0.07, fc='m')

def init():
    bob.center = (0.1, 0.1)
    ax.add_patch(bob)
    return bob,

def animate(i):
    x_position = l*np.sin(theta_points[i]) 
    y_position = l*np.cos(theta_points[i]) 
    bob.center = (x_position, y_position)
    return bob,

plt.title('An epic non-linear pendulum',fontsize=15)
plt.xlabel('x', fontsize=13)
plt.ylabel('y',fontsize=13)

ani = animation.FuncAnimation(fig, animate,
init_func=init, frames=360, interval=20, blit=True)

#saves creation
ani.save('pendulum.gif', writer='pillow')

plt.show()   