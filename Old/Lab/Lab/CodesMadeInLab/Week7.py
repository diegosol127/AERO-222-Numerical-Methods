# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:10:32 2021

@author: allendavism
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:05:20 2021

@author: allen
"""
### HW 3
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def dfdx(f,x,y,z,h = 1e-8):
    df = (f(x+h,y,z)-f(x-h,y,z))/(2.*h)
    return df
def dfdy(f,x,y,z,h = 1e-8):
    df = (f(x,y+h,z)-f(x,y-h,z))/(2.*h)
    return df
def dfdz(f,x,y,z,h = 1e-8):
    df = (f(x,y,z+h)-f(x,y,z-h))/(2.*h)
    return df
def Jacobian(funcs,x,y,z):
    J = np.zeros((len(funcs),len(funcs)))
    ii = 0
    for f in funcs:
        # breakpoint()
        J[ii][0] = dfdx(f,x,y,z)
        J[ii][1] = dfdy(f,x,y,z)
        J[ii][2] = dfdz(f,x,y,z)
        ii += 1
    return J

# def fP1(x): return np.sin(3*x)

# def f1(x,c1,c2,c3,c4): return c1*x + c2*x + c3*(2*x**2) + c4*(4*x**3-3*x)

# def f2(x,c1,c2,c3,c4): 
#     return c1*np.sin(x**2) + c2*(1-np.cos(x)) + c3*(np.cos(x)*np.sin(x)) + c4*(2.-x)/(2+x)


xk = np.linspace(-1,1,100)



### Problem 4
def f11(x,y,z=1):    return x**2-2*y**2-3*z
def f22(x,y,z=1):    return -x**2 + 2*y**3-np.exp(-z)+1
def f33(x,y,z=1):    return x + 2*y**2+3*z

def twoNorm4(xList,yList,zList=[]):
    if len(xList) < 2:
        twoNorm = 10
    else:
        twoNorm = (xList[-1]-xList[-2])**2
        twoNorm += (yList[-1]-yList[-2])**2
        if len(zList) > 0:
            twoNorm += (zList[-1]-zList[-2])**2
        twoNorm = twoNorm**0.5
    return twoNorm

x4 = 1
y4 = 1
z4 = 1

eps = 1e-6
xL4 = [x4]
yL4 = [y4]
zL4 = [z4]
fxL1= [f11(x4,y4)]
fxL2 = [f22(x4,y4)]
fxL3 = [f33(x4,y4)]
iL = [1]
iteration = 1
twoNorm = 10
while twoNorm > eps:
    iteration += 1
    J = Jacobian([f11,f22,f33],x4,y4,z4)
    fk = np.array([f11(x4,y4,z4),f22(x4,y4,z4),f33(x4,y4,z4)])
    [x4,y4,z4] = [x4,y4,z4] - np.matmul(np.linalg.inv(J),fk)
    xL4.append(x4)
    yL4.append(y4)
    zL4.append(z4)
    fxL1.append(f11(x4,y4,z4))
    fxL2.append(f22(x4,y4,z4))
    fxL3.append(f33(x4,y4,z4))
    twoNorm = twoNorm4(xL4,yL4,zL4)
    iL.append(iteration)
    print(twoNorm)

d4 = np.transpose([iL,xL4,yL4,fxL1,fxL2,fxL3])
headers = ['Iteration','x','y','f1','f2','f3']
print(tabulate(d4,headers=headers))
