n=int(input())
l=[]
l=input().split(' ')
for i in range(len(l)):
    l[i]=int(l[i])
l.sort(reverse=True)
sum=0
for i in range(len(l)):
    sum+=int(l[i])
sum/=2
tsum=0
coinnum=0
for j in range(len(l)):
    tsum+=int(l[j])
    if tsum>sum:
        coinnum=j+1
        break
    else:
        pass
print (coinnum)
