import numpy as np
import matplotlib.pyplot as plt

eps = 0.001
def f1(x):
	out = x*x-4*x-6
	return out

def f2(x):
	out = (4*x+5)**0.5
	return out

def f3(x):
	out = 5/(x-4)
	return out

def fx1(x):
	output = (2.*x+3)**0.5
	return output

def fx2(x):
	output = 3./(x-2)
	return output

def fx3(x):
	output = 0.5*(x**2-3)
	return output



x1 = 5
residual = 1
rList = []
while residual > eps:
	x2 = fx3(x1)
	residual = abs(x2-x1) 
	rList.append(residual)
	length1 = len(rList)
	if rList[length1-1] > rList[length1-2]:
		break
	x1 = x2

### --------------------- FIXED POINT ITERATION
x1 = 3
residual2 = 1
rList2 = []
while residual2 > eps:
	x2 = f3(x1)
	residual2 = abs(x2-x1) 
	x1 = x2

x0 = 4
x1 = -4
### ---------------------------- BISECTION METHOD
b = x0
a = x1
xL = []
e1L = []
while (b-a) > eps:
	xMid = (a+b)/2.
	if np.sign(f1(xMid)) == np.sign(f1(a)):
		a = xMid
	else:
		b = xMid
	xL.append(xMid)
	e1L.append(abs(f1(xMid)))
	print(xMid)

### ------------------------------- SECANT METHOD ----------------------
error = 1.
xnm = x0
xn = x1-f1(x1)*(x1-x0)/(f1(x1)-f1(x0))
x2L = [xnm]
e2L = []
while error > eps:
	xnp = xn-f1(xn)*(xn-xnm)/(f1(xn)-f1(xnm))
	xnm = xn
	xn = xnp
	x2L.append(xn)
	error = abs(f1(xn))
	e2L .append(error)
	print(error,xn)

### -Regula-Falsi
a3 = x1
b3 = x0
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

plt.plot(e1L,'r',label='Bisection Method')
plt.plot(e2L,'b',label='Secant Method')
plt.plot(e3L,'g',label='Regula-Falsi Method')
plt.xlabel('Iteration')
plt.ylabel('p(x)')
plt.legend()