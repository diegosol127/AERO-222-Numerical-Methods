
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

### Problem 1
def f1(x): return 5*np.cos(10*x)+x**3-2*x**2-6*x+10
def df1(x): return -50*np.sin(10*x) + 3*x**2 - 4*x - 6

def forw1(x,f,i,h=np.pi/8): return (1*f[i+0]-2*f[i+1]+1*f[i+2])/(1*1.0*h**2)
def forw2(x,f,i,h=np.pi/8): return (-3*f[i-1]-10*f[i+0]+18*f[i+1]-6*f[i+2]+1*f[i+3])/(12*1.0*h**1)
def cent1(x,f,i,h=np.pi/8): return (1*f[i-2]-8*f[i-1]+0*f[i+0]+8*f[i+1]-1*f[i+2])/(12*1.0*h**1)
def back1(x,f,i,h=np.pi/8): return (-1*f[i-3]+6*f[i-2]-18*f[i-1]+10*f[i+0]+3*f[i+1])/(12*1.0*h**1)
def back2(x,f,i,h=np.pi/8): return (3*f[i-4]-16*f[i-3]+36*f[i-2]-48*f[i-1]+25*f[i+0])/(12*1.0*h**1)

xList1 = np.linspace(0,4,100)
fx =  [f1(val) for val in xList1]
dfx = [df1(val) for val in xList1]
df1 = []
xList = xList1
for i in range(len(xList)):
	if i < 1:
		val = forw1(xList[i],fx,i,h=xList[1]-xList[0])
	elif i < 2:
		val = forw2(xList[i],fx,i,h=xList[1]-xList[0])
	elif i < len(xList)-3:
		val = cent1(xList[i],fx,i,h=xList[1]-xList[0])
	elif i < len(xList)-2:
		val = back1(xList[i],fx,i,h=xList[1]-xList[0])
	elif i < len(xList)-1:
		val = back2(xList[i],fx,i,h=xList[1]-xList[0])
	df1.append(val)
error1 = [abs(df1[i]-dfx[i]) for i in range(len(df1))]
plt.semilogy(xList,error1)
plt.xlabel('X')
plt.ylabel('Error')
plt.show()
plt.close()

### Problem 4
def f(x):   return x+np.sin(x)
def df(x):  return 1+np.cos(x)
def ddf(x): return -np.sin(x)

xList = np.linspace(0,4,100)
hList = np.linspace(-.5,.5,1000)
ddfx = [ddf(val) for val in xList]

def back4(x,f,h=np.pi/8): return (f(x-2*h)-2*f(x-h)+f(x))/h**2
def forw4(x,f,h=np.pi/8): return (f(x-0*h)-2*f(x+1*h)+f(x+2*h))/h**2
def cent4(x,f,h=np.pi/8): return (f(x-1*h)-2*f(x-0*h)+f(x+1*h))/h**2

ddf1 = ddf(1.0)
b4 = back4(1.0,f)
f4 = forw4(1.0,f)
c4 = cent4(1.0,f)
table = [["Backwards","Central","Forwards"],
		 [abs(b4-ddf1),abs(c4-ddf1),abs(f4-ddf1)]]
print(tabulate(table))
backddf = [back4(1.0,f,h=i) for i in hList]
centddf = [cent4(1.0,f,h=i) for i in hList]
forwddf = [forw4(1.0,f,h=i) for i in hList]
errorB = abs(backddf-ddf1)
errorC = abs(centddf-ddf1)
errorF = abs(forwddf-ddf1)
plt.semilogy(hList,errorB,label='Backward')
plt.semilogy(hList,errorC,label='Central')
plt.semilogy(hList,errorF,label='Forward')
plt.xlabel('dx')
plt.ylabel('Error')
plt.legend()
plt.show()
plt.close()

### Problem 5
T = [80,44.5, 30, 24.1, 21.7, 20.7]
t = [0,5,10,15,20,25]
h = 5
der = []
for i in range(len(T)):
	if i <1:
		f_x = (-3*T[i+0]+4*T[i+1]-1*T[i+2])/(2*1.0*h**1)
	if 0 < i and i < 5:
		f_x = (-1*T[i-1]+0*T[i+0]+1*T[i+1])/(2*1.0*h**1)
	if i > 4:
		f_x = (1*T[i-2]-4*T[i-1]+3*T[i+0])/(2*1.0*h**1)
	der.append(f_x)
table = [["t",t],["T",T],["T'",der]]
print(tabulate(table))