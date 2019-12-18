import numpy as np

import astropy.constants as c
import astropy.units as u

import matplotlib.pyplot as plt

"Potential and Electric Charge"

#Defining variables
E0 = c.eps0.value   #Epsilon
r = 0.01            #Radius
q1 = 1              #Positive Charge
q2 = -1             #Negative Charge

#Function of potential depending on charge and radius
def potential(q,r):
    phi=(1/(4*np.pi*e0)*q/r)
    return phi

N = 100                     #Grid number
pot = np.zeros([N,N])       #Array of potential filled with zeros 
x = np.linspace(0,1, num=N) #Range along the x
y = x                       #Range of y is same as x

#Initial points
xp = [0.45,0.55] #Initial x_point, Final x_point
yp = [0.50,0.50] #initial y_point, Final y_point

#Nested for loop 
for i in range(N):
    for j in range(N):

        x_local = x[j]
        y_local = y[i]
        R1 = np.sqrt((x_local-xp[0])**2+(y_local-yp[0])**2)
        R2 = np.sqrt((x_local-xp[1])**2+(y_local-yp[1])**2)
        
        pot[i][j] = (1/(4*np.pi*E0)*(q1/R1))+(1/(4*np.pi*E0)*(q2/R2))

#Plot of charges/potentials 
map=plt.imshow(pot)
map.set_cmap("viridis")
plt.title("lovely charges", fontsize=15)
plt.show()

#Single step 
h = 1/N

#Electric field arrays
E_x = np.zeros([N,N]) #Electric field array for x
E_y = np.zeros([N,N]) #Electric field array for y

#Nested for loop 
for i in range(1,N-1):
    for j in range(1,N-1):
        
        #Using central difference formula to calculate respective derivatives
        partialx = (pot[i+1][j] - pot[i-1][j])/(2*h) #Central difference for x components
        partialy = (pot[i][j+1] - pot[i][j-1])/(2*h) #Central difference for y components
        E_x[i][j] = partialx
        E_y[i][j] = partialy

#Zooms in
scale=1e-13 

#Set figure
fig,ax=plt.subplots()
fig.suptitle('electric field :)', fontsize=15, fontweight='bold')

#For loop
for i in range(1,N,10):
    for j in range(1,N,10):

        #Electric field plot 
        plt.arrow(x[j],y[i],scale*E_x[i][j],scale*E_y[i][j], lw='3')

ax.set_xlim([0,1]) #Adjusts x-limit between 0 and 1
ax.set_ylim([0,1]) #Adjusts y-limit between 0 and 1
plt.show()