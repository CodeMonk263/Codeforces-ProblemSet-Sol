n=int(input())
ar1=[]
for i in range(n):
    x=input()
    ar1.append([0,1])
    a,b=x.split(' ')
    ar1[i][0],ar1[i][1]=a,b

maxi=0
tsum=0
temp=0
for j in range(n):
    temp=int(ar1[j][1])-int(ar1[j][0])
    tsum+=temp
    if tsum>maxi:
        maxi=tsum
print(maxi)  
    
