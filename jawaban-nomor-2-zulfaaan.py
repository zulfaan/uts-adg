# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 23:10:04 2021

@author: 5_kewajiban
"""

import pandas as pd
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

#Membaca data excel 
Excel = pd.read_excel('Data_Nomor1.xlsx', header=1, names=None, usecols="A:C")

#Data yang digunakan
N = Excel['Geophone'].to_numpy()
x = Excel['Ts'].to_numpy()
y = Excel['Depth'].to_numpy()

#Bannyaknya data sampel
N = len(N)
dt=1.66 #time increment in each data
#FFT
fft=rfft(y)*dt
freq=rfftfreq(N,d=dt)
FFT=abs(fft)

plt.plot(freq,FFT, label = 'signal')
plt.grid()
plt.xlabel('Frequency')
plt.ylabel(r'Amplitude')
plt.legend(loc=1)
plt.show()