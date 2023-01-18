# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:01:36 2021

@author: allendavism
"""

import numpy as np
import matplotlib.pyplot as plt


def f1(x):
	out = x*x-2.*x-3
	return out

def g1(x):
	output = (2.*x+3)**0.5
	return output

def g2(x):
	output = 3./(x-2)
	return output

e0 = 1.

x00 = 4.5
eps = 0.001


error1 = e0
x0 = x00
xL1 = [x0]
eL1 = []
while error1 > eps:
	x1 = g1(x0)
	x2 = g1(x1)
	x = x0 - (x1-x0)**2. / (x2-2.*x1+x0)
	error1 = abs(x-x2)
	xL1.append(x)
	eL1.append(error1)
	x0 = x

error2 = e0
x0 = x00
xL2 = [x0]
eL2 = []
while error2 > eps:
	x1 = g2(x0)
	x2 = g2(x1)
	x = x0 - (x1-x0)**2. / (x2-2.*x1+x0)
	error2 = abs(x-x2)
	xL2.append(x)
	eL2.append(error2)
	x0 = x


x1 = x00
residual = e0
rList = []
xList = [x1]
while residual > eps:
	x2 = g1(x1)
	residual = abs(x2-x1) 
	rList.append(residual)
	xList.append(x2)
	length1 = len(rList)
	if rList[length1-1] > rList[length1-2]:
		break
	x1 = x2


x1 = x00
residual2 = e0
rList2 = []
xList2 = [x1]
while residual2 > eps:
	x2 = g2(x1)
	residual2 = abs(x2-x1) 
	rList2.append(residual2)
	xList2.append(x2)
	length1 = len(rList2)
	x1 = x2

plt.new_figure_manager(1)
plt.plot(xL1, label = 'G1, Aitken')
plt.plot(xList, label = 'G1, Fixed-Point')
plt.plot(xL2, label = 'G2, Aitken')
plt.plot(xList2, label = 'G2, Fixed-Point')
plt.ylabel('Root')
plt.xlabel('Iteration')
plt.legend()
# plt.close()

# plt.new_figure_manager(2)

# plt.plot(eL1, label = 'G1, Aitken')
# plt.plot(rList, label = 'G1, Fixed-Point')
# plt.plot(eL2, label = 'G2, Aitken')
# plt.plot(rList2, label = 'G2, Fixed-Point')
# plt.ylabel('Error')
# plt.xlabel('Iteration')
# plt.legend()

