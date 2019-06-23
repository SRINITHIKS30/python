num=int(input())
numArray= []
sameNum=[]
for i in range (0,num):
  numArray.append(int(input()))   

for i in range (0,num):
    if(numArray[i]==i):
        sameNum.append(numArray[i])
if(len(sameNum)==0):
    print("-1")
else:
    for i in range (0,len(sameNum)):
        print(sameNum[i])
