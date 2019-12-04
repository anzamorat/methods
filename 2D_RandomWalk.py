"2-Dimensional Random Walk"

#Necessary packages/modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 1000000 #Amount of steps to pass in my for loop

#Empty arrays to fill up later (through for loop)
x = np.zeros(N) #Array for my x-values
y = np.zeros(N) #Array for my y-values

#Choices of the 4 distinct paths
random_walk = ('up','down','right','left')

#For loop 
for i in range(1,N): 
    
    direction = np.random.choice(random_walk) #Random generator choosing directon (R,L,U,D)

    #Conditions for path chosen
    if direction == 'right': 
        x[i] = x[i - 1] + 1 #Particle goes right (x-coordinate increases)
        y[i] = y[i - 1] 
        
    elif direction == 'left': 
        x[i] = x[i - 1] - 1 #Particle goes left (x-coordinate decreases)
        y[i] = y[i - 1] 
        
    elif direction == 'up': 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1 #Particle goes up (y-coordinate increases)
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1 #Particle goes down (y-coordinate decreases)

"ANIMATION TIME !!!"

#Create figure
fig = plt.figure(figsize=(6,5))
fig.suptitle('2D-Brownian Motion', fontsize=15, fontweight='bold')
ax = plt.axes(xlim=(-50,50), ylim=(-50,50)) #Axes with limits
ax.set_title('random walk ($N = ' + str(N) + '$ steps)')

#Patch for animation
Particle = plt.Circle((0, 0), radius=1.7, fc='c') #Circle shape to depict particle

#Initialization of animation
def init():
    Particle.center = (0, 0)
    ax.add_patch(Particle)
    return Particle,

#Movement of particle to be animated beginning from center of particle
def animate(i):
    x_position = x[i]
    y_position = y[i]
    Particle.center = (x_position, y_position)
    return Particle,

#Lets put it all together & animate this whole thing!
ani = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)

#Shows figure (sometimes)
fig.show()

#Saves creation
ani.save('final_brownian.mp4')
