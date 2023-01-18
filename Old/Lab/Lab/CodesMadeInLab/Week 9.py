# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:04:06 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt
x = [-3,1,3,-2,4]
y = [1,3,4,2,8]

def f1(a,b,x,y): return a*np.exp(x*b) - y
def f2(a,b,x): return a*np.exp(x*b)
def df1a(a,b,x,y): return np.exp(b*x)
def df1b(a,b,x,y): return a*x*np.exp(b*x)

a,b  = 0.1,0.1
aL = [a]
bL = [b]
eps = 10e-7
error = 10
while error > eps:
    Jac = np.zeros((5,2))
    fv = []
    for ii in range(5):
        Jac[ii][0] = df1a(a,b,x[ii],y[ii])
        Jac[ii][1] = df1b(a,b,x[ii],y[ii])
        fv.append( f1(a,b,x[ii],y[ii]))
    Jt = np.matrix.transpose(Jac)
    anew,bnew = [a,b] - np.matmul(np.linalg.inv(np.matmul(Jt,Jac)),np.matmul(Jt,fv))    
    error = ((anew-a)**2+(bnew-b)**2)**0.5
    a = anew
    b = bnew
    print(anew,bnew,error)
    
xl = np.linspace(-4,4,300)
f2
f1x = [f2(a,b,xl[ii]) for ii in range(len(xl))]
plt.plot(xl,f1x)
plt.plot(x,y,'.')
plt.show()