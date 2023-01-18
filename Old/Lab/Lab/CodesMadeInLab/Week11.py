# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:26:31 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
def f(x):   return x+np.sin(x)
def df(x):  return 1+np.cos(x)
def ddf(x): return -np.sin(x)

xList = np.linspace(0,4,100)
hList = np.linspace(-.5,.5,1000)

def forw1(x,f,i,h=np.pi/8): return (1*f[i+0]-2*f[i+1]+1*f[i+2])/(1*1.0*h**2)
def cent1(x,f,i,h=np.pi/8): return (1*f[i-1]-2*f[i+0]+1*f[i+1])/(1*1.0*h**2)
def back1(x,f,i,h=np.pi/8): return (1*f[i-2]-2*f[i-1]+1*f[i+0])/(1*1.0*h**2)
fx =  [f(val) for val in xList]
dfx = [df(val) for val in xList]

# fError = forw1(1.0,f)

ddfx = [ddf(val) for val in xList]

def back4(x,f,h=np.pi/8): return (f(x-2*h)-2*f(x-h)+f(x))/h**2
def forw4(x,f,h=np.pi/8): return (f(x-0*h)-2*f(x+1*h)+f(x+2*h))/h**2
def cent4(x,f,h=np.pi/8): return (f(x-1*h)-2*f(x-0*h)+f(x+1*h))/h**2

ddf1 = ddf(1.0)
b4 = back4(1.0,f)
f4 = forw4(1.0,f)
c4 = cent4(1.0,f)
table = [["Backwards","Central","Forwards"],
		 [abs(b4-ddf1),abs(c4-ddf1),abs(f4-ddf1)]]

print(tabulate(table))

backddf = [back4(1.0,f,h=i) for i in hList]
centddf = [cent4(1.0,f,h=i) for i in hList]
forwddf = [forw4(1.0,f,h=i) for i in hList]
errorB = [abs(backddf[i]-ddfx) for i in range(len(backddf))]
errorB = abs(backddf-ddf1)
errorC = abs(centddf-ddf1)
errorF = abs(forwddf-ddf1)
plt.semilogy(hList,errorB,label='Backward')
plt.semilogy(hList,errorC,label='Central')
plt.semilogy(hList,errorF,label='Forward')
plt.xlabel('dx')
plt.ylabel('Error')
plt.legend()

