# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:37:26 2021

@author: allendavism
"""
import numpy as np
def f1(x):
	output = x**2- 3*x+3
	return output

eps = 0.001
a3 = -5
b3 = 5
error = 1.
x3L = []
e3L = []
while error > eps:
	xrfp = b3 - f1(b3)*(b3-a3)/(f1(b3)-f1(a3))
	x3L.append(xrfp)
	fx = f1(xrfp)
	error = abs(fx)
	e3L.append(error)
	if np.sign(f1(xrfp)) == np.sign(f1(a3)):
		a3 = xrfp
	else:
		b3 = xrfp