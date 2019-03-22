import numpy as np
import cmath as c
import matplotlib.pyplot as plt
#j=c.sqrt(-1)
def dft(x1,N):
	k=np.arange(0,N)
	n1=np.arange(0,N)
	z=len(x1)
	if z<N:
		q=N-z
		x1=np.append(x1,np.zeros(q))
	y=[]
	M=[]
	P=[]
	for i in k:
		sum=0;
		for j in n1:
			sum+=x1[j]*np.exp(-1*2*np.pi*1j*i*j/np.float(N))
		y.append(sum)
		
	return y
N=input("number of dft ponts")
x=input("enter values1")#ex:a=[1,2,3]
n=input("enter number of shift")
z=len(x)
if z<N:
	q=N-z
	x=np.append(x,np.zeros(q))
print x
c=len(x)
print c
x1=[]
for i in range(c):
	a=x[(c+i-n)%N]
	x1.append(a)
print x1
M=dft(x1,N)
P=dft(x,N)
k=np.arange(0,N)
Q=[]
for i in  k:
	a=P[i]*np.exp(-1*2*np.pi*1j*i*n/np.float(N))
	Q.append(a)
M1=(np.abs(M))
P1=(np.angle(M))
#print P1
M2=(np.abs(Q))
P2=(np.angle(Q))
plt.subplot(411)
plt.plot(M1)
plt.subplot(412)
plt.plot(P1)
plt.subplot(413)
plt.plot(M2)
plt.subplot(414)
plt.plot(P2)
plt.show()
