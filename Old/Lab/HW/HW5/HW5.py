# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:58:58 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from scipy import integrate
### Problem 1
def fI(x): return np.exp(2*x)*np.cos(3*x)
a,b = 0, np.pi
sol = -2/13*(1+np.exp(2*np.pi))
n = list(range(5, 21))
integral,error,trapI,trapE = [],[],[],[]
for jj in n:
	xList = np.linspace(a,b,jj+1)
	part = 0
	for ii in range(jj):
		part += fI((xList[ii+1]+xList[ii])/2.)
	integral.append((b-a)/jj*part)
	error.append((b-a)/jj*part-sol)
	trap = fI(a)+fI(b)
	for ii in range(1,jj):
		trap += 2*fI(xList[ii])
	trapI.append(1./2*(b-a)/jj*trap)
	trapE.append(abs(trapI[-1]-sol))
plt.plot(n,integral,label='Midpoint')
plt.plot(n,trapI,label='Trapezoid')
plt.xlabel('Number of Partitions')
plt.ylabel('Integral')
plt.legend()
plt.show()
plt.close()

plt.semilogy(n,error,label='Midpoint')
plt.semilogy(n,trapE,label='Trapzoid')
plt.xlabel('Number of Partitions')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()

### Problem 2

c2 = (trapI[3]-trapI[2])/((b-a)**2/49 - (b-a)**2/64)
Ire1 = trapI[2] + c2*(b-a)**2/49
Ire2 = trapI[3] + c2*(b-a)**2/64

table2 = [['n','I_{t}','I_{Re}'],[7,trapI[2],Ire1],[8,trapI[3],Ire2]]
print(tabulate(table2))

### Problem 3
def f3(x): return 1/(2+x**2)
sol3 = 2**0.5*np.arctan(1/(2**0.5))
a3,b3 = -1,1
int3, err3 = [], []

for jj in range(3,13):
	n3 = jj
	x3 = np.linspace(a3,b3,n3*2+1)
	part3 = f3(a3)+f3(b3)
	for k in range(n3):
		part3+=4*f3(x3[2*k+1])
	for k in range(1,n3):
		part3 +=2*f3(x3[2*k])
	int3.append((b-a)/(6*n3)*part3)
	err3.append(abs(int3[-1]-sol3))

plt.semilogy(range(3,13),err3)
plt.xlabel('Number of Partitions')
plt.ylabel('Error')
plt.show()
plt.close()

### Problem 4
def f4(t):	 return 2000*np.log(110000/(110000-1600*t))-9.8*t
a4,b4 = 2,20
x = [[-0.775,0.775,0,0,0,0],
	 [-0.861,0.861,-0.400,0.400,0,0],
	 [-0.906,0.906,-0.538,0.538,0,0] ]
w = [[.556,.556,.889,0,0,0],
	 [.348,.348,.652,.652,0,0],
	 [.237,.237,.479,.479,.569,0]]
I4 = []
for n4 in range(3,6):
	I = 0
	for ii in range(n4):
		I += w[n4-3][ii]*f4((x[n4-3][ii]+1)*(b4-a4)/2+a4)*(b4-a4)/2
	I4.append(I)

table = [['3 Point','4 Point','5 Point'],I4]
print(tabulate(table))

### Problem 5
# Euler's Method
n51 = 30
x130 = np.linspace(1,4,n51)
x230 = np.linspace(0,3,n51)
x1300 = np.linspace(1,4,300)
x2300 = np.linspace(0,3,300)
error130,error230,error1300,error2300 = [0],[0],[0],[0]
true1 = [2*x51**3 for x51 in x130]
true2 = [0.25*(2*x52+5*np.exp(-2*x52)-1) for x52 in x230]
true3 = [2*x51**3 for x51 in x1300]
true4 = [0.25*(2*x52+5*np.exp(-2*x52)-1) for x52 in x2300]
y130 = [2]
y230 = [1]
y1300 = [2]
y2300 = [1]
h1 = 3/(n51-1)
h2 = 3/299
for ii in range(n51-1):
	term1 = 3/x130[ii]*y130[ii]
	term2 = x230[ii]-2*y230[ii]
	y130.append(y130[ii]+h1*term1)
	y230.append(y230[ii]+h1*term2)
	error130.append(abs(y130[-1]-true1[ii+1]))
	error230.append(abs(y230[-1]-true2[ii+1]))

for ii in range(299):
	term1 = 3/x1300[ii]*y1300[ii]
	term2 = x2300[ii]-2*y2300[ii]
	y1300.append(y1300[-1]+h2*term1)
	y2300.append(y2300[-1]+h2*term2)
	error1300.append(abs(y1300[-1]-true3[ii+1]))
	error2300.append(abs(y2300[-1]-true4[ii+1]))

plt.plot(x130,y130,label='30 steps, Equation 1, Eulers Method')
plt.plot(x1300,y1300,label='300 steps, Equation 1, Eulers Method')
plt.plot(x130,true1,label='True Solution')
plt.legend()
plt.show()
plt.close()

plt.plot(x230,y230,label='30 steps, Equation 2, Eulers Method')
plt.plot(x2300,y2300,label='300 steps, Equation 2, Eulers Method')
plt.plot(x230,true2,label='True Solution')
plt.legend()
plt.show()
plt.close()

plt.semilogy(x130,error130,label='30 steps, Equation 1, Eulers Method')
plt.semilogy(x1300,error1300,label='300 steps, Equation 1, Eulers Method')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()

plt.semilogy(x2300,error2300,label='300 steps, Equation 2, Eulers Method')
plt.semilogy(x230,error230,label='30 steps, Equation 2, Eulers Method')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()

### Problem 6
def f61(x,y): return 3*y/x
def f62(x,y): return x-2*y


y61,y610 = [2],[2]
y62,y620 = [1],[1]
e61,e62,e610,e620 = [0],[0],[0],[0]
for ii in range(n51-1):
	k11 = h1*f61(x130[ii],y61[ii])
	k21 = h1*f61(x130[ii]+h1/2,y61[ii]+k11/2)
	k31 = h1*f61(x130[ii]+h1/2,y61[ii]+k21/2)
	k41 = h1*f61(x130[ii]+h1,y61[ii]+k31)
	y61.append(y61[-1]+(k11+2*k21+2*k31+k41)/6)
	e61.append(abs(y61[-1]-true1[ii+1]))
	k12 = h1*f62(x130[ii],y62[ii])
	k22 = h1*f62(x130[ii]+h1/2,y62[ii]+k12/2)
	k32 = h1*f62(x130[ii]+h1/2,y62[ii]+k22/2)
	k42 = h1*f62(x130[ii]+h1,y62[ii]+k32)
	y62.append(y62[-1]+(k12+2*k22+2*k32+k42)/6)
	e62.append(abs(y62[-1]-true2[ii+1]))

for ii in range(299):
	k11 = h2*f61(x1300[ii],y610[ii])
	k21 = h2*f61(x1300[ii]+h1/2,y610[ii]+k11/2)
	k31 = h2*f61(x1300[ii]+h1/2,y610[ii]+k21/2)
	k41 = h2*f61(x1300[ii]+h1,y610[ii]+k31)
	y610.append(y610[-1]+(k11+2*k21+2*k31+k41)/6)
	e610.append(abs(y610[-1]-true3[ii+1]))
	k12 = h2*f62(x1300[ii],y620[ii])
	k22 = h2*f62(x1300[ii]+h1/2,y620[ii]+k12/2)
	k32 = h2*f62(x1300[ii]+h1/2,y620[ii]+k22/2)
	k42 = h2*f62(x1300[ii]+h1,y620[ii]+k32)
	y620.append(y620[-1]+(k12+2*k22+2*k32+k42)/6)
	e620.append(abs(y620[-1]-true4[ii+1]))

sci1 = integrate.solve_ivp(f61,[1,4],[2],max_step=h1)
sci2 = integrate.solve_ivp(f62,[0,3],[1],max_step=h2)

plt.semilogy(x230,e61,label='30 steps, Equation 1')
plt.semilogy(x2300,e610,label='300 steps, Equation 1')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()

plt.semilogy(x230,e62,label='30 steps, Equation 2')
plt.semilogy(x2300,e620,label='300 steps, Equation 2')
plt.ylabel('Runge-Kutta Error')
plt.legend()
plt.show()
plt.close()

plt.plot(x130,y130,label='30 steps, Equation 1')
plt.plot(x1300,y1300,label='300 steps, Equation 1')
plt.plot(x130,true1,label='True Solution')
plt.plot(sci1.t,sci1.y[0],label='Scipy Solution')
plt.ylabel('Runge-Kutta Solutions')
plt.legend()
plt.show()
plt.close()

plt.plot(x230,y230,label='30 steps, Equation 2')
plt.plot(x2300,y2300,label='300 steps, Equation 2')
plt.plot(x230,true2,label='True Solution')
plt.plot(sci2.t,sci2.y[0],label='Scipy Solution')
plt.ylabel('Runge-Kutta Solutions')
plt.legend()
plt.show()
plt.close()