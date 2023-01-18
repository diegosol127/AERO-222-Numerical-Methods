from math import factorial
import matplotlib.pyplot as plt
import numpy as np

truth = np.exp(-4)
e1 = 0
e2 = 0
error1 = []
error2 = []

for k in range(0,8):
	e1 += ((-1.)**k)*(4.**k)/(factorial(k))
	e2 += (4**k)/(factorial(k))
	error1.append(abs(truth-e1))
	error2.append(abs(truth-1./e2))

plt.plot(error1,label='Method 1')
plt.plot(error2,label='Method 2')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.legend()