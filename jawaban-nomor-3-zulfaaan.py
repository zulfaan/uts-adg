# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 00:12:50 2021

@author: Zulfa Nurfajar
"""

from obspy import read
import matplotlib.pyplot as plt
import numpy as np

#membaca data gempa
st1 = read("IU.PMSA.00.BH1.M.2021-09-28T070719.019538.txt")
st2 = read("IU.WCI.00.BH1.M.2021-09-28T070905.019538.txt")
st3 = read("IU.YAK.00.BH1.M.2021-09-28T070300.019538.txt")
  
#memvisualisasikan data gempa
st1.plot()
st2.plot()
st3.plot()

#transformasi ke dalam domain frekuensi
#untuk IU.PMSA.00.BH1
Data_PMSA =[]
for i in range(len(st1)):
    Data2 = st1[i].data
    Data_PMSA.append(Data2)
Datafft_PMSA = []
for i in range(len(Data_PMSA)):
    datafft = np.fft.rfft(Data_PMSA[i])
    Datafft_PMSA.append(datafft)
    plt.figure(i+1)
    plt.plot(abs(Datafft_PMSA[i]),linewidth=0.5)
    plt.title(str(st1[i]))
    plt.xlabel('Freq(Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    

#untuk IU.WCI.00.BH1
Data_WCI =[]
for i in range(len(st2)):
    Data2 = st2[i].data
    Data_WCI.append(Data2)
Datafft_WCI = []
for i in range(len(Data_WCI)):
    datafft = np.fft.rfft(Data_WCI[i])
    Datafft_WCI.append(datafft)
    plt.figure(i+1)
    plt.plot(abs(Datafft_WCI[i]),linewidth=0.5)
    plt.title(str(st2[i]))
    plt.xlabel('Freq(Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    
    
#untuk IU.YAK.00.BH1
Data_YAK =[]
for i in range(len(st3)):
    Data2 = st3[i].data
    Data_YAK.append(Data2)
Datafft_YAK = []
for i in range(len(Data_YAK)):
    datafft = np.fft.rfft(Data_YAK[i])
    Datafft_YAK.append(datafft)
    plt.figure(i+1)
    plt.plot(abs(Datafft_YAK[i]),linewidth=0.5)
    plt.title(str(st3[i]))
    plt.xlabel('Freq(Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    
