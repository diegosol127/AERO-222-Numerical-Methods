import numpy as np
def f(x):
    output = x**2 + 6*x
    return output
eps = 0.001
a = 5 
b = -5
error = abs(f(a))
while error > eps:
    RF = b - (f(b)*(b-a))/(f(b)-f(a))
    if np.sign(f(RF)) == np.sign(f(a)):
        a = RF
    else:
        b = RF
    error = abs(f(RF))
    print(RF)