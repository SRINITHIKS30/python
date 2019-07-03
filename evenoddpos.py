# your code goes here
n=int(input())
a=[]
b=[]
for i in range(0,int(n)):
    a.append(int(input()))
for i in range(0,n):
    if i%2==0 and int(a[i])%2!=0:
        b.append(a[i])
    elif i%2!=0 and int(a[i])%2==0:
    	b.append(a[i])
print(b)
