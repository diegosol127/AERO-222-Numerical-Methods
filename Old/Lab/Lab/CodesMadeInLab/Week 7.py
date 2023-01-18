# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:29:53 2021

@author: allendavism
"""
import numpy as np
def f1(x,y,z): return 2*x+y+z
def f2(x,y,z): return 3*x-y-z**2
def f3(x,y,z): return 3.2*x+y**2-2*z

def dfdx(f,x,y,z,h=1e-8):
    dx = (f(x+h,y,z)-f(x-h,y,z))/(2.*h)
    dy = (f(x,y+h,z)-f(x,y-h,z))/(2.*h)    
    dz = (f(x,y,z+h)-f(x,y,z-h))/(2.*h)
    return dx,dy,dz
def Jacobian(funcs,x,y,z):
    J = np.zeros((len(funcs),len(funcs)))
    ii = 0
    for f in funcs:
        J[ii][:] = dfdx(f,x,y,z)
        ii += 1
    return J
def twoN(A):
    two = 0
    for row in A:
        two += (row[-1]-row[-2])**2
    return two**0.5

x,y,z = 1,1,1
xL,yL,zL,eL = [x],[y],[z],[]
eps = 10e-6
error = 10
while error > eps:
    J = Jacobian([f1,f2,f3],x,y,z)
    [x,y,z] = [x,y,z] - np.matmul(np.linalg.inv(J),[f1(x,y,z),f2(x,y,z),f3(x,y,z)])
    xL.append(x)
    yL.append(y)
    zL.append(z)
    twoNorm = twoN([xL,yL,zL])
    eL.append(twoNorm)
    error = twoNorm
    print(x,y,z)