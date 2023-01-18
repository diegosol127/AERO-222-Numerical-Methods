import numpy as np
import matplotlib.pyplot as plt

eps = 0.001
def f1(x):
	out = x*x-3*x-5
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
xList = []
xList.append(x1)
while residual > eps:
	x2 = fx2(x1)
	residual = abs(x2-x1) 
	rList.append(residual)
	xList.append(x2)
	length1 = len(rList)
	if rList[length1-1] > rList[length1-2]:
		break
	x1 = x2
	
x1 = 5
residual = 1
rList2 = []
xList2 = [x1]
while residual > eps:
	x2 = fx1(x1)
	residual = abs(x2-x1) 
	rList2.append(residual)
	xList2.append(x2)
	length1 = len(rList2)
	if rList2[length1-1] > rList2[length1-2]:
		break
	x1 = x2

x1 = 5
residual = 1
rList3 = []
xList3 = [x1]
while residual > eps:
	x2 = fx3(x1)
	residual = abs(x2-x1) 
	rList3.append(residual)
	xList3.append(x2)
	length1 = len(rList3)
	if rList3[length1-1] > rList3[length1-2]:
		break
	x1 = x2

plt.plot(xList,label='g1(x)')
plt.plot(xList2,label='g2(x)')
plt.plot(xList3,label='g3(x)')
plt.xlabel('Iteration')
plt.ylabel('X')
plt.legend()
plt.show()
plt.close()

plt.semilogy(rList,label='g1(x)')
plt.semilogy(rList2,label='g2(x)')
plt.semilogy(rList3,label='g3(x)')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()

### -Regula-Falsi
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

plt.plot(e3L,'g',label='Regula-Falsi Method')
plt.xlabel('Iteration')
plt.ylabel('p(x)')
plt.legend()