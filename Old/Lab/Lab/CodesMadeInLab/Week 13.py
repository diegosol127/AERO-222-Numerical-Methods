import numpy as np
import matplotlib.pyplot as plt

def fI(x): return np.exp(2*x)*np.cos(3*x)
a,b = 0, np.pi
sol = -2/13*(1+np.exp(2*np.pi))
n = list(range(5, 21))
integral,error = [], []
for jj in n:
	xList = np.linspace(a,b,jj+1)
	part = 0
	for ii in range(jj):
		part += fI((xList[ii+1]+xList[ii])/2.)
	integral.append((b-a)/jj*part)
	error.append((b-a)/jj*part-sol)

plt.plot(n,integral)
plt.xlabel('Number of Slices')
plt.ylabel('Integral')
plt.show()
plt.close()

plt.semilogy(n,error)
plt.xlabel('Number of Slices')
plt.ylabel('Error')
plt.show()
plt.close()

### Legandre

def f4(t):	 return 2000*np.log(110000/(110000-1600*t))-9.8*t
def f5(x): return (x-1)*np.sin(x**2)
a4,b4 = 2,20
x = [[-0.7746,0.7746,0,0,0,0],
	 [-0.861,0.861,-0.400,0.400,0,0],
	 [-0.906,0.906,-0.538,0.538,0,0] ]
w = [[.556,.556,.889,0,0,0],
	 [.348,.348,.652,.652,0,0],
	 [.237,.237,.479,.479,.569,0]]

for n4 in range(3,6):
	I = 0
	for ii in range(n4):
		I += w[n4-3][ii]*f4(x[n4-3][ii])
I2 = 0
n2 = 3
for ii in range(n2):
	I2 += w[n2-3][ii]*f5(x[n2-3][ii])