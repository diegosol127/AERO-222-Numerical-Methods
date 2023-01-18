import matplotlib.pyplot as plt
def quad(x):
	result = x**2 - 2*x - 3
	return result
def dydx(x,tol=0.001):
	fx0 = quad(x-tol)
	fx1 = quad(x+tol)
	fPrime = ((fx1-fx0)/(2.*tol))
	return fPrime

def dydx2(x,tol = 0.001):
	result = 2*x - 2
	return result

x0 = -4.5
residual =  1
tol2 = 0.01
tol1 = 1e-5
totalResidual = []
xL1 = []
while residual > tol1:
	x = x0
	fx = quad(x)
	fPrime = dydx(x,tol2)
	x0 = x - fx/fPrime
	error = abs(x-x0)
	residual = abs(quad(x0))
	totalResidual.append(residual)
	xL1.append(x0)
	print('Residual = '+str(residual))	
	
totalResidual2 = []
xL2 = []
residual = 1
x0 = 4.5
while residual > tol1:
	x = x0
	fx = quad(x)
	fPrime = dydx(x,tol2)
	x0 = x - fx/fPrime
	error = abs(x-x0)
	residual = abs(quad(x0))
	totalResidual2.append(residual)
	xL2.append(x0)
	print('Residual = '+str(residual))	
	
	
	
plt.plot(totalResidual,label='X_0 = 4.5')
plt.plot(totalResidual2,label='X_0 = -4.5')
plt.xlabel('Iteration')
plt.ylabel('Residual')
plt.legend()
plt.show()
plt.close()

plt.plot(xL1,label='X_0 = -4.5')
plt.plot(xL2,label='X_0 = 4.5')
plt.xlabel('Iteration')
plt.ylabel('Root')
plt.legend()