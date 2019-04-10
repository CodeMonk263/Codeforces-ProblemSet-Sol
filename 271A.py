n=int(input())
n+=1
ctr=0
def i2l(k):
    x=[]
    while(k>0):
        t=k%10
        x.append(t)
        k=k//10
    x.reverse()
    return x


while 1000<=n<=9100:
    i=[]
    i=i2l(n)
    for j in range(4):
        for k in range(4):
            if ((i[j]==i[k]) and (j!=k)):
                ctr+=1

    if ctr==0:
        break
    else:
        n+=1
        ctr=0
print(n)
