# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:40:08 2021

@author: allen
"""
import numpy as np
import matplotlib.pyplot as plt
n = 50
x = np.linspace(3,6,n+1)
h = 3/n
y = [2]
for ii in range(n):
	term1 = 2*y[ii]/(x[ii]**2)
	y.append(y[ii]+h*term1)
plt.plot(x,y) 
