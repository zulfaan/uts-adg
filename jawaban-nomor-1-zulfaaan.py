# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:04:35 2021

@author: Zulfa Nurfajar
"""
import pandas as pd
import matplotlib.pyplot as plt

#Membaca data excel 
Excel = pd.read_excel('Data_Nomor1.xlsx', header=1, names=None, usecols="B:C")

#Memplot sinyal kontinu kedalaman dan waktu
x = Excel['Ts'].to_numpy()
y = Excel['Depth'].to_numpy()

#grafik waktu dan kedalaman
plt.plot(x,y)
plt.xlabel('Time (s)')
plt.ylabel('Depth')
plt.grid('True')
plt.title('Kedalaman Terhadap Waktu')
plt.show()



