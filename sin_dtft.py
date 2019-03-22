import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
w=np.arange(0,10*np.pi,0.5)
x=5*(np.sin(w))
k=x
c=0
a=[]
r=np.linspace(-np.pi,np.pi,1000)
for i in range(1000):
	en=r[i]
	for d in range(0,len(k)):
		c=c+(k[d]*np.exp((-(j*r[i]*d))))
	a.append(c)
	c=0
q=np.abs(a)
p=np.angle(a)
plt.subplot(4,1,1)
plt.plot(r,a)
plt.subplot(4,1,2)
plt.plot(r,q)
plt.subplot(4,1,3)
plt.plot(r,p)
plt.subplot(4,1,4)
plt.plot(w,x)
plt.show()
