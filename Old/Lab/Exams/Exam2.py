# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:54:12 2021

@author: allendavism
"""
import numpy as np

x1 = [-1,0,2]
y1 = [np.pi, -1,5]
### Lagrangian Interpolation based on all x and y values
def L1(x1,y1,xval) :
	Lx = 0
	for kk in range(len(x1)):
		num = 1
		den = 1
		for ii in range(len(x1)):
			if ii != kk:
				num = num*(xval-x1[ii])
				den = den*(x1[kk] - x1[ii])
		Lx += num/den*y1[kk]
	return Lx

def L2(x1,y1,xval) :
	Lrow = []
	for kk in range(len(x1)):
		num = 1
		den = 1
		for ii in range(len(x1)):
			if ii != kk:
				num = num*(xval-x1[ii])
				den = den*(x1[kk] - x1[ii])
		Lrow.append(num/den)
	return Lrow

xval = L1(x1,y1,1)

### Problem 3
x3 = [-1,0,2]
y3 = [np.pi,-1,5]
A = [[np.sin(x3[0]), np.exp(-x3[0]**3),1+x3[0]-x3[0]**2],
	 [np.cos(x3[1]), -3*x3[1]*np.exp(-x3[1]**3), 1-2*x3[1]],
	 [np.sin(x3[2]), np.exp(-x3[2]**3),1+x3[2]-x3[2]**2]
	  ]

Ainv = np.linalg.inv(A)
sol = np.matmul(Ainv,y3)
### Problem 4
x4,y4,z4 = 3,3,3
trace = z4*np.cos(x4*z4)+y4**2 - 2*y4+x4*z4-2*z4

### Problem 5
A5Tinv = [[0.0091,0],[0,0.5]]
A5T = [[np.pi**2, np.pi**2/4, np.pi**2/4],
	   [0,1,-1]]
b5 = [-1,-0.5,.5]

Atb = np.matmul(A5T,b5)
[alpha,beta] = np.matmul(A5Tinv,Atb)