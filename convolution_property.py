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
x1=input("take x values") #ex:[1,2,3]
x2=input("take y values") 
z1=len(x1)
z2=len(x2)
if z1<N:
	q1=N-z1
	x1=np.append(x1,np.zeros(q1))
if z2<N:
	q2=N-z2
	x=np.append(x2,np.zeros(q2))
u=[]
for n in range(N):
	q=0
	for k in range(N):
		q +=x1[k]*(x2[(n-k)%N])
	u.append(q)	
print u
M=dft(u,N)
M1=dft(x1,N)
M2=dft(x2,N)
e=len(M1)
print e
M3=[]
for i in range(e):
	a=M1[i]*M2[i]
	M3.append(a)
R1=(np.abs(M))
R2=(np.angle(M))
R3=(np.abs(M3))
R4=(np.angle(M3))
plt.subplot(411)
plt.plot(R1)
plt.subplot(412)
plt.plot(R2)
plt.subplot(413)
plt.plot(R3)
plt.subplot(414)
plt.plot(R4)
plt.show()

