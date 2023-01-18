### HW 1
from math import factorial
import matplotlib.pyplot as plt
import numpy as np

def Problem1():
	def f1(x):
		out = x*x-4*x-6
		return out

	x0 = 4
	x1 = -4
	eps = 0.001
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
# 		print(xMid)
	
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
# 		print(error,xn)
	
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
	plt.show()
	plt.close()


def Problem2():
	def f1(x):
		output = 2.32*x**3 + 2.08*x**2 - 4.86*x + 8.33
		return output
	
	def f2(x):
		output = round(8.33 - round(4.86*x,3) + round(2.08*round(x**2,3),3) + round(2.32*round(x**3,3),3),3)
		return output
	
	def f3(x):
		output = round(round(round(round(round(round(2.32*x,3)+2.08,3)*x,3) - 4.86,3)*x,3)+8.33,3)
		return output
	
	x = 1.35
	solution1 = f1(x)
	round1 = f2(x)
	roundNest = f3(x)
	
	absError = abs(solution1-round1)
	relError = abs(solution1-round1)/solution1
	
	absErrorNest = abs(solution1-roundNest)
	relErrorNest = abs(solution1-roundNest)/solution1
	
	print('Machine Precision Yields: '+ str(solution1))
	print('Rounding to 3 sig figs yields an absolute error of: ' + str(absError))
	print('Rounding to 3 sig figs yields a relative error of: ' + str(relError))
	print('Rounding to 3 sig figs nested yields an absolute error of: ' + str(absErrorNest))
	print('Rounding to 3 sig figs nested yields a relative error of: ' + str(relErrorNest))



def Problem3():
	truth = np.exp(-4)
	e1 = 0
	e2 = 0
	error1 = []
	error2 = []
	v1 = []
	v2 = []
	v11 = []
	v12 = []
	for k in range(0,8):
		e1 += ((-1.)**k)*(4.**k)/(factorial(k))
		e2 += (4**k)/(factorial(k))
		v1.append( ((-1.)**k)*(4.**k)/(factorial(k)))
		v2.append((4**k)/(factorial(k)))
		error1.append(abs(truth-e1))
		error2.append(abs(truth-1./e2))
		v11.append(e1)
		v12.append(e2)
	plt.plot(error1,label='Method 1')
	plt.plot(error2,label='Method 2')
	plt.xlabel('Iteration')
	plt.ylabel('Error')
	plt.legend()
	plt.show()
	plt.close()
	print('Method one yields an error of: ',str(error1[-1]))
	print('Method two yields an error of: ',str(error2[-1]))


def Problem4():
	def eq4(x0,x1):
		output = x0**3 + np.cos(x0) +(3*x0**2-np.sin(x0))*(x1-x0) + (6*x0 - np.cos(x0))*(x1-x0)**2/(factorial(2)) + (6+np.sin(x0))*(x1-x0)**3/(factorial(3))
		return output
	P4a = eq4(4,3.4)
	P4b = eq4(3,3.1)
	print('Problem 4 part a solution: '+str(P4a))
	print('Problem 4 part b solution: '+str(P4b))

def Problem7():
	def p7z(x,y):
		output = 2*x-y+np.sin(x*y**2)
		return output
	def p7w(z):
		output = np.exp(z) - 2*(z-1)
		return output
	x = 2
	y = 1
	dwdz = np.exp(p7z(x,y)) - 2
	dzdx = 2. + np.cos(x*y**2)*y**2
	dzdy = -1. + 2.*y*x*np.cos(x*y**2)
# 	breakpoint()
	sigx = 0.03
	sigy = 0.01
# 	dwdz = 47.85
# 	dzdx = 1.584
# 	dzdy = -2.665
	z = p7z(x,y)
	w = p7w(z)
	sigz = (dzdx**2*sigx**2 + dzdy**2 * sigy**2)**0.5
	print('Problem 7 mu_{w} = '+str(w))
	sigmaw = (dwdz**2 * sigz**2)**0.5
	print('Problem 7 sigma_{z} = '+str(sigz))
	print('Problem 7 sigma_{w} = '+str(sigmaw))

Problem1()
Problem2()
Problem3()
Problem4()
Problem7()