b=int(input())
lb=input().split(' ')

for i in range(len(lb)):
    lb[i]=int(lb[i])
print(lb)
g=int(input())
lg=input().split(' ')

for i in range(len(lg)):
    lg[i]=int(lg[i])
print(lg)

ans=0

for x in range(b):
    temp=lb[x]
    for y in range(g):
        if (abs(temp-lg[y])<=1):
            ans+=1
            lb.pop(x)
            lg.pop(y)
            break

print(ans)
