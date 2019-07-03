n=int(input())
a=[]
for i in range(0,n):
    a.append(input())
x=len(a)
for i in range(0,x-1):
    c=0
    n=a[i]
    for j in range(0,x):
        if i!=j:
            if a[i]==a[j]:
                c=c+1
                n=a[i]
    if c==0:
        print(n)
