n=int(input())
a=[]
b=[]
t=0
for i in range(0,n):
    a.append(input())
for i in range(0,n):
    b.append(0)
for i in range(0,n-1):
    c=0
    for j in range(i+1,n):
        if(a[i]==a[j]):
            t=1
            b[j]=a[j]
if t!=1:
    print("unique")
else:
    for i in b:
        if i!=0:
            print(i)
            break
