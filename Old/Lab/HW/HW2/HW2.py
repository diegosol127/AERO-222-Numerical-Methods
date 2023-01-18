# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:42:32 2021

@author: allendavism
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as linalg

def func1(x):return (x+1)**0.5 + 1 - np.exp(x)
def dfdx1(x,h):return (func1(x)-func1(x-h))/(h)

x = 0
h = 1e-7
eps = 10**-12
xL = []
eL = []
iter1 = 0
while abs(func1(x)) > eps:
	xNew = x - func1(x)/dfdx1(x,h)
	x = xNew
	xL.append(x)
	eL.append(abs(func1(x)))
	iter1 += 1
print(str(iter1)+' Iterations using Residual')
	
x = 0
xL2 = []
eL2 = []
iter2 = 0
errorOld = 10
errorNew = 9
while errorNew < errorOld:
	errorOld = errorNew
	xNew = x - func1(x)/dfdx1(x,h)
	errorNew = abs(xNew-x)
	x = xNew
	xL2.append(x)
	eL2.append(abs(errorNew-errorOld))
	iter2 += 1
	
print(str(iter2)+' Iterations using Error')

plt.plot(eL,'.-',label='Part 1')
plt.semilogy(eL2,'.-',label='Part 2')
plt.legend()
plt.xlabel('Iteration Number')
plt.ylabel('Convergence Criteria')
plt.show()
plt.close()

### Problem 2
a2 = np.array([[1,3,1],[2,2,-6],[3,-1,2]])
b2 = np.array([-1,2,3])
xP2 = np.linalg.solve(a2,b2)

x1 = xP2[0]
x2 = xP2[1]
x3 = xP2[2]

x21 = x1 + 3*x2 + x3
x22 = 2*x1 + 2*x2 - 6*x3
x23 = 3*x1 - 1*x2 + 2*x3
print('r1 = '+str(x21)+', r2 = '+str(x22)+', r3 = ' + str(x23))


### Problem 3
def f3(l):return 1.289 - (1+(l-1)/2*0.7**2)**(l/(l-1))
def df3(l,h): return (f3(l+h)-f3(l))/h

eps = 1e-12
x0 = 0
error = abs(f3(x0))
h = 1e-5
iter3 = 0
while error > eps:
	x1 = x0 - f3(x0)/df3(x0,h)
	x0 = x1
	error = abs(f3(x0))
	iter3 += 1
print('Final Residual = ' + str(error) + ', Final Root = ' + str(x1))


### Problem 4

def g14(x):	return 1/(x-10)
def g24(x):	return (x**2-1)/10
def g34(x):	return(10*x+1)**0.5

def getDG(f4,x,h): return abs((f4(x+h)-f4(h))/h)


gL1 = []
gL2 = []
gL3 = []
h = 1e-7
vals = np.linspace(-3,3,100)
for val in vals:
	gL1.append(getDG(g14,val,h))
	gL2.append(getDG(g24,val,h))
	gL3.append(getDG(g34,val,h))

plt.plot(vals,gL1,label='G1 prime')
plt.plot(vals,gL2,label='G2 prime')
plt.plot(vals,gL3,label='G3 prime')
plt.legend()
plt.show()
plt.close()
### -------------------- Problem 5 ------------------------------------- ###


def f5(x):	return -x**4 + 2*x**3 - np.exp(-x) + 1
def df5(x):return -4*x**3 + 6*x**2 + np.exp(-x)
def ddf5(x):return -12*x**2 + 12*x - np.exp(-x)

def g5(x):return abs(f5(x)*(ddf5(x))/(df5(x)**2))


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


### Problem 6

b6 = [-1,3,5,-6,3]
A6 = np.array([[3,4,7,-1,4],
				 [6,-2,0,2,-2],
				 [4,1,-1,2,4],
				 [2,10,-6,-4,1],
				 [5,3,-1,-8,3]])

Am = np.array([[6,-2,0,2,-2,3],
			   [3,4,7,-1,4,-1],
				 [4,1,-1,2,4,5],
				 [2,10,-6,-4,1,-6],
				 [5,3,-1,-8,3,3]])
Amat = A6
[m,n] = np.shape(Amat)

def Upper(aug):
	[n,m] = np.shape(aug)
	for jj in range(n):
		for ii in range(n):
			if ii > jj:
				aug[ii][:] = aug[ii][:] - aug[ii][jj]/aug[jj][jj]*aug[jj][:]
				aug[ii][:] = aug[ii][:]/aug[ii][jj+1]
	return aug

def Lower(aug):
	[n,m] = np.shape(aug)
	for kk in range(-n+1,1):
		for ll in range(-n+1,1):
			ii = -kk
			jj = -ll
			if ii < jj:
				aug[ii][:] = aug[ii][:] - aug[ii][jj]/aug[jj][jj]*aug[jj][:]
				aug[ii][:] = aug[ii][:]/aug[ii][jj-1]
	return aug

Amat2 = Amat
for jj in range(n):
	for ii in range(m):
		if ii > jj and abs(Amat[jj][jj]) > 1e-10:
			Amat[ii][:] = Amat[ii][:] - Amat[ii][jj]/Amat[jj][jj]*Amat[jj][:]

LU6 = linalg.lu(A6)
Ainv = np.linalg.inv(A6)
x6 = linalg.solve(A6,b6)

### Problem 7

b7 = [3,-1,2]
a7  = np.array([[3,-1,2],[1,3,1],[2,2,-6]])
def Diag(A):
	[n,m] = np.shape(A)
	A2 = np.zeros((n,m))
	A2Inv = np.zeros((n,m))
	for ii in range(n):
		for jj in range(m):
			if ii == jj:
				A2[ii][jj] = A[ii][jj]
				A2Inv[ii][jj] = 1./A[ii][jj]
	return A2,A2Inv
def twoNorm(x1,x0):
	norm1 = 0
	norm2 = 0
	for ii in range(len(x1)):
		norm1 += (x1[ii]-x0[ii])**2
		norm2 += x1[ii]**2
	norm1 = norm1**0.5
	norm2 = norm2**0.5
	norm = norm1/norm2
	return norm

D7,Di7 = Diag(a2)
O7 = a7-D7
x7 = np.matmul(Di7,b2)
nL7 = []
xL7 = []
iter7 = 0
error = 1
while error > 1e-12:
	xNew = np.matmul(Di7,b7) - np.matmul(np.matmul(Di7,O7),x7)
	error = twoNorm(xNew,x7)
	x7 = xNew
	nL7.append(error)
	xL7.append(xNew)
	iter7 += 1
	print(xNew,error,iter7)
