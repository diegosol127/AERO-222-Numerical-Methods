# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:22:45 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt

def y(x):
	out = np.exp(100*x)
	return out

def dy(x):
	out = 100*np.exp(100*x)
	return out

def getError(h,x):
	true = dy(x)
	estimate = (y(x+h)-y(x))/h
	error = abs((true-estimate)/true)
	return error
hList = []
eList = []
pts = 150
x = 5
for n in range(pts):
	h = 0.001/(10**(n/(pts/15)))
	error = getError(h,x)
	hList.append(h)
	eList.append(error)

plt.loglog(hList,eList,'r')
plt.xlabel('h')
plt.ylabel('error')