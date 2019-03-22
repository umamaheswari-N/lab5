import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
n=input("enter x length:")
k=[]
for i in range(n):
	z=input("enter x elements:")
	k.append(z)
c=0
a=[]
w=np.linspace(-np.pi,np.pi,1000)
for i in range(1000):
	en=w[i]
	j=cm.sqrt(-1)
	for d in range(0,n,1):
		c=c+(k[d]*np.exp((-(j*en*d))))
	a.append(c)
	c=0
q=np.abs(a)
p=np.angle(a)
plt.subplot(3,1,1)
plt.plot(w,a)
plt.subplot(3,1,2)
plt.plot(w,q)
plt.subplot(3,1,3)
plt.plot(w,p)
plt.show()
