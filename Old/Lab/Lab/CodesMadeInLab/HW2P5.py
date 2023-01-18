# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:53:32 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt
### -------------------- Problem 5 ------------------------------------- ###


def f5(x):
	output = -x**4 + 2*x**3 - np.exp(-x) + 1
	return output
def df5(x):
	output = -4*x**3 + 6*x**2 + np.exp(-x)
	return output
def ddf5(x):
	output = -12*x**2 + 12*x - np.exp(-x)
	return output

def g5(x):
	output = abs(f5(x)*(ddf5(x))/(df5(x)**2))
	return output

x0 = 1.6
x5 = [x0]
e5 = []
for ii in range(5):
	x1 = x0 - f5(x0)/df5(x0)
	x5.append(x1)
	e5.append(abs(x1-x0))
	x0 = x1

ran = np.linspace(-3,3,100)
gList = []
for val in ran:
	gList.append(g5(val))

plt.semilogy(ran,gList)
plt.xlabel('X')
plt.ylabel('dG(x)/dx')
plt.show()
plt.close()


alpha5 = (np.log(e5[-1])-np.log(e5[-2]))/(np.log(e5[-2])-np.log(e5[-3]))
lam5 = e5[-1]/(e5[-2]**alpha5)