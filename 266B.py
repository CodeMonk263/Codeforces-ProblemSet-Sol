i=input().split(' ')
n,t=int(i[0]),int(i[1])

s=input()
ls=list(s)

def switch(x):
    k=0
    while(k<n-1):
        if (x[k]=='B' and x[k+1]=='G'):
            x[k]='G'
            x[k+1]='B'
            k+=2
        else:
            k+=1
    return x

for j in range(t):
    ls=switch(ls)
    
s=''.join(ls)
print(s)

