import numpy as np
import matplotlib.pyplot as plt

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
plt.xlabel('Number of Slices')
plt.ylabel('Integral')
plt.legend()
plt.show()
plt.close()

plt.semilogy(n,error,label='Midpoint')
plt.semilogy(n,trapE,label='Trapzoid')
plt.xlabel('Number of Slices')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()
