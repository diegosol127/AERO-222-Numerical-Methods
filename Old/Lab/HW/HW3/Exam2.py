import numpy as np
x = np.array([0.0234, 1.1868, 3.7149, 3.8821])
y = np.array([-2.3603, 0.8476, 5.4382, 11.9204])
z = np.array([1.5045, 1.7633, 1.9391, 2.0038])
def function1(c,x,y):    return c[0] + c[1]*x + c[2]*y
A = np.zeros((len(x),3))
for ii in range(4):
	A[ii][0] = 1
	A[ii][1] = x[ii]
	A[ii][2] = y[ii]
At = np.transpose(A)  
c = np.matmul(np.linalg.inv(np.matmul(At,A)),np.matmul(At,z)) 
fx = function1(c,x,y)



