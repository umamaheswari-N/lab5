import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=[1,2,3,4,5,6]
N=len(x)
p=N-1
m=5
u=N+m
y=[]
while(N<u):
	x.append(0)
	N=N+1
y.append(x)
print(y)
j=cm.sqrt(-1)
n=np.arange(0,p,1)
k=np.arange(0,p,1)
c=0
g=[]
for k in range(p):
	for n in range(p):
		c=c+(x[n]*np.exp((-(j*2*np.pi*k*n/N))))
	g.append(c)
	c=0
print(g)
h=np.abs(g)
e=np.angle(g)
plt.subplot(4,1,1)
plt.stem(h)
plt.subplot(4,1,2)
plt.stem(e)
plt.subplot(4,1,3)
plt.stem(g)
plt.subplot(4,1,4)
plt.stem(x)
plt.show()
