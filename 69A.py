n=int(input())
xch,ych,zch=0,0,0
l=[]
for i in range(n):
    l.append([])
    l[i]=[int(x) for x in input().split()]
   
for k in range(n):
    xch+=l[k][0]
    ych+=l[k][1]
    zch+=l[k][2]
if xch==0 and ych==0 and zch==0:
    print("YES")
else:
    print("NO")
