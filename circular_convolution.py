x=input("take x values") #ex:[1,2,3]
h=input("take y values") 
z=len(x)
u=[]
for n in range(z):
	q=0
	for k in range(z):
		q +=x[k]*(h[(n-k)%z])
	u.append(q)	
print u