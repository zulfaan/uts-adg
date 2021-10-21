# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 23:55:41 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

#Membaca data excel 
Excel = pd.read_excel('Data_Nomor1.xlsx', header=1, names=None, usecols="A:C")

#Data yang digunakan
N = Excel['Geophone'].to_numpy()
x = Excel['Ts'].to_numpy()
y = Excel['Depth'].to_numpy()

#FFT
#Bannyaknya data sampel
N = len(N)
#Frekuensi sinyal dalam sehari
T = 1
#perform FFT on signal
yf = fft(y)
#data frekuensi (x)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#plot results
plt.plot(xf, yf[0:N//2], label = 'signal')
plt.grid()
plt.xlabel('Frequency')
plt.ylabel(r'Amplitude')
plt.legend(loc=1)
plt.show()
