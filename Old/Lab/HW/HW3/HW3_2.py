# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:43:38 2021

@author: allen
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x): return np.sin(3.*x)


x = np.linspace(-1,1,100)
fx = np.array([f(c) for c in x])
fc = fx + np.random.normal(0,.08,100)


plt.plot(x,fx,label='f(x)')
plt.plot(x,fc,label='fc(x)')
plt.legend()
plt.show()
plt.close()

A1 = np.zeros((len(x),4))
A2 = np.zeros((len(x),4))

for ii in range(len(x)):
    A1[ii][0] = 1
    A1[ii][1] = x[ii]
    A1[ii][2] = 2.*x[ii]**2-1
    A1[ii][3] = 4.*x[ii]**3-3.*x[ii]
    
for ii in range(len(x)):
    A2[ii][0] = np.sin(x[ii]**2)
    A2[ii][1] = 1.-np.cos(x[ii])
    A2[ii][2] = np.cos(x[ii])*np.sin(x[ii])
    A2[ii][3] = (2.-x[ii])/(2.+x[ii])
At1 = np.transpose(A1)    
At2 = np.transpose(A2)    
c1 = np.matmul(np.linalg.inv(np.matmul(At1,A1)),np.matmul(At1,fc)) 
c2 = np.matmul(np.linalg.inv(np.matmul(At2,A2)),np.matmul(At2,fc)) 

def f1(c,x):    return c[0]*1 + c[1]*x+c[2]*(2.*x**2-1)+c[3]*(4.*x**3-3.*x)
def f2(c,x):    return c[0]*np.sin(x**2)+c[1]*(1.-np.cos(x))+c[2]*(np.cos(x)*np.sin(x))+c[3]*(2.-x)/(2.+x)

f1y = np.array([f1(c1,point) for point in x])
f2y = np.array([f2(c2,point) for point in x])

def norm1(x):
    out = 0
    for val in x:
        out += abs(val)
    return out

def norm2(x):
    out = 0
    for val in x:
        out += val**2
    out = out**0.5
    return out

def norm3(x):   return max(abs(x))
    

Norm1 = [norm1((f1y-fx)),norm1((f2y-fx))]
Norm2 = [norm2((f1y-fx)),norm2((f2y-fx))]
Norm3 = [norm3((f1y-fx)),norm3((f2y-fx))]
plt.plot(x,f1y,label='f1')
plt.plot(x,f2y,label='f2')
plt.legend()
plt.show()
plt.close()