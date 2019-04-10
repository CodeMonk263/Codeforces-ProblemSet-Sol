x=input().split(' ')
f=input().split(' ')
n=int(x[0])
m=int(x[1])
for i in range(len(f)):
    f[i]=int(f[i])

for j in range(len(f)):
    for k in range(0,len(f)-j-1):
        if (f[k]>f[k+1]):
            t=f[k]
            f[k]=f[k+1]
            f[k+1]=t

a=f[0]
b=f[n-1]
ans=abs(a-b)
for i in range(len(f)):
    for j in range(len(f)):
        if abs(f[i]-f[j])<ans:
            ans=abs(f[i]-f[j])


print(ans)

