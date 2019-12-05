import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal

"One cycle of a square-wave"

#Setting conditions
N = 10**3
a = 0
b = 1

def square_wave(t):
    
    #Boundaries for the amplitude of the wave to become 1
    if int(2*t)%2 == 1: 
        return 1       #Return one
    else:
        return 0       #Return zero otherwise

#Creating equally spaced values between 0 and 1 w/ evenly spaced N points
t_points=np.linspace(a,b,N) #Range of time points
values=[]                   #Empty list to fill of values

#For loop appending values to function of square_wave
for t in t_points:
    values.append(square_wave(t)) 

plt.plot(values, c='k', lw='3')
plt.title('Square-Wave Function (\u03BB vs. $t$)', fontsize=15, fontweight='bold')
plt.xlabel('Time', fontsize=13)
plt.ylabel('Amplitude', fontsize=13)
plt.show()

"Fourier Transform of Square-Wave"

#Fourier transforming the sawtooth with fft module
DFT_square = fft(values)

#Final values of square-wave
final_square = DFT_square*np.conjugate(DFT_square)

plt.plot(np.abs(DFT_square), c='k', lw='3')
plt.title('Square-Wave Function (\u03BB vs. $f$ )', fontsize=15, fontweight='bold')
plt.xlabel('Frequency', fontsize=13)
plt.ylabel('Amplitude', fontsize=13)
plt.xlim(0,30) #Zoomed in
plt.show()

"Sawtooth"

#Creating equally spaced valaues between 0 and 1 with N evenly spaced points
t = np.linspace(0, 1, N) 
#Used signal module in scipy to display sawtooth
sawtooth = signal.sawtooth(2*np.pi*5*t) 

plt.plot(sawtooth, c='r', lw='2')
plt.title('Sawtooth (\u03BB vs. $t$)', fontsize=15, fontweight='bold')
plt.xlabel('Time', fontsize=13)
plt.ylabel('Amplitude', fontsize=13)
plt.show()

"Fourier Transform of Sawtooth"

#Fourier transforming the sawtooth with fft module
DFT_sawtooth = fft(sawtooth)

#Taking the conjugate to get rid of imaginary values
final_sawtooth = DFT_sawtooth*np.conjugate(DFT_sawtooth)

#Plotting 
plt.plot(t, np.abs(final_sawtooth), c='r', lw='2') #Taking the absolute value to be on the safe side
plt.title('Sawtooth (\u03BB vs. $f$ )', fontsize=15, fontweight='bold')
plt.xlabel('Frequency', fontsize=13)
plt.ylabel('Amplitude', fontsize=13)
plt.xlim(0,0.5) #Zooms in
plt.show()

"Modulated Sine Wave"

n = np.arange(0,N) #Individual time-point
sin = np.sin(np.pi*n/(N))*np.sin(20*np.pi*n/(N)) #Formula for this unique sine wave

#Ploting regular graph of sine wave 
plt.plot(n,sin)
plt.title('Modulated Sine Wave (\u03BB vs. $t$)', fontsize=15, fontweight='bold')
plt.xlabel('Time', fontsize=13)
plt.ylabel('Amplitude', fontsize=13)
plt.show()

"Fourier Transform of Modulated Sine Wave"

#Discrete fourier "transforming" it
DFT_sin = fft(sin) 
#Final sine wave values to be pplotted
final_sin = DFT_sin*np.conjugate(DFT_sin) 

#Plotting modulated sine wave yn = sin(πn/N) sin(20πn/N)
plt.plot(np.abs(final_sin))
plt.title('Modulated Sine Wave (\u03BB vs. $f$ )', fontsize=15, fontweight='bold')
plt.xlabel('Frequency', fontsize=13)
plt.ylabel('Amplitude', fontsize=13)
plt.xlim(0,200)
plt.show()
