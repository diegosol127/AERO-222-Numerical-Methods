### HW 4

import numpy as np
import matplotlib.pyplot as plt

x1 = [-1.83, -1.11, 0.18, 0.90, 2.05]
y1 = [15.6, 12.4, 5.6, 8.4, 7.5]
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

T1 = np.zeros((len(x1),len(y1)))
for ii in range(len(x1)):
	for jj in range(len(x1)):
		T1[ii][:] = L2(x1,y1,x1[ii])

xList = np.linspace(-3,3,100)
interpList = []
for xval in xList:
	interpList.append(L1(x1,y1,xval))
plt.plot(x1,y1,'.',label='Real Values')
plt.plot(xList,interpList,label='Interpolation')
plt.legend()
plt.show()
plt.close()