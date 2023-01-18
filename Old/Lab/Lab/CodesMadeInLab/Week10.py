# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:25:27 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt

x =[0,1,3,-2,-4]
y = [1,3,4,5,1]

def getT(x,y,xval):
    T = np.zeros((len(x),len(y)))
    num = 1
    den = 1
    L = []
    for k in range(len(x)):
        for i in range(len(x)):
            if i != k:
                num *= xval-x[i]
                den *= x[k]-x[i]                
        L.append( num/den)
    return L
def fullL(x,y,xval):
    L = 0
    for ii in range(len(x)):
        L += getT(x,y,xval)[ii]*y[ii]
    return L

T = []
for xval in x:
    T.append(getT(x,y,xval))

xL = np.linspace(-4,3,200)
yL = []
for xval in xL:
    yL.append(fullL(x,y,xval))
plt.plot(xL,yL)
plt.plot(x,y,'.')
