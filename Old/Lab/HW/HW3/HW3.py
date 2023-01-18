# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:05:20 2021

@author: allen
"""
### HW 3
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


### Problem 1
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
    return out**0.5

def norm3(x):   return max(abs(x))

Norm1 = [norm1((f1y-fx)),norm1((f2y-fx))]
Norm2 = [norm2((f1y-fx)),norm2((f2y-fx))]
Norm3 = [norm3((f1y-fx)),norm3((f2y-fx))]
plt.plot(x,f1y,label='f1')
plt.plot(x,f2y,label='f2')
plt.legend()
plt.show()
plt.close()


### Problem 2
x2 = [1,2,3,5]
y2 = [-1,1,0,1]
xval = 4
Lx = 0
for kk in range(4):
    num =1
    den = 1
    for ii in range(4):
        if ii != kk:
            num = num*(xval-x2[ii])
            den = den*(x2[kk] - x2[ii])
    Lx += num/den*y2[kk]
    
print('Legrange = ' +str(Lx))

def f2(c,x):    return c[0]*np.sin(x)+c[1]*(1-x**2)+5*c[2]*(np.cos(x)/(x+1))+c[3]*3
Ap2 = np.zeros((4,4))
for ii in range(4):    
    Ap2[ii][0] = np.sin(x2[ii]) 
    Ap2[ii][1] = 1-x2[ii]**2
    Ap2[ii][2] = 5*np.cos(x[ii])/(x2[ii]+1)
    Ap2[ii][3] = 3

Ap2t = np.transpose(Ap2)  
cP21 = np.matmul(np.linalg.inv(np.matmul(Ap2t,Ap2)),np.matmul(Ap2t,y2)) 
fxP2 = f2(cP21,xval)
print('Least squares = '+str(fxP2))

### Problem 3
def dfdx(f,x,y = 0,h = 1e-8):
    df = (f(x+h,y)-f(x-h,y))/(2.*h)
    # print(df)
    return df
def dfdy(f,x,y = 0,h = 1e-8):
    df = (f(x,y+h)-f(x,y-h))/(2.*h)
    return df

def Jacobian(funcs,x,y=0):
    J = np.zeros((len(funcs),len(funcs)))
    ii = 0
    for f in funcs:
        # breakpoint()
        J[ii][0] = dfdx(f,x,y)
        J[ii][1] = dfdy(f,x,y)
        ii += 1
    return J


### Problem 4
def f14(x,y):
    return x**2-y**2-1
def f24(x,y):
    return -x**2 + 2*y**3-np.exp(-x*y)+1
def twoNorm4(xList,yList):
    if len(xList) < 2:
        twoNorm = 10
    else:
        twoNorm = (xList[-1]-xList[-2])**2
        twoNorm += (yList[-1]-yList[-2])**2
        twoNorm = twoNorm**0.5
    return twoNorm

x4 = 3
y4 = 4
eps = 1e-6
xL4 = [x4]
yL4 = [y4]
fxL14 = [f14(x4,y4)]
fxL24 = [f24(x4,y4)]
iL = [1]
iteration = 1
twoNorm = 10
while twoNorm > eps:
    iteration += 1
    J = Jacobian([f14,f24],x4,y4)
    fk = np.array([f14(x4,y4),f24(x4,y4)])
    [x4,y4] = [x4,y4] - np.matmul(np.linalg.inv(J),fk)
    xL4.append(x4)
    yL4.append(y4)
    fxL14.append(f14(x4,y4))
    fxL24.append(f24(x4,y4))
    twoNorm = twoNorm4(xL4,yL4)
    iL.append(iteration)
    # print(twoNorm)

d4 = np.transpose([iL,xL4,yL4,fxL14,fxL24])
headers = ['Iteration','x','y','f1','f2']
print(tabulate(d4,headers=headers))
