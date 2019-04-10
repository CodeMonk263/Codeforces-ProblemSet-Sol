n=int(input())
l=[]
for i in range(n):
    l.append([])
    l[i]=[]
    l[i]=input().split(' ')
    for j in range(2):
        l[i][j]=int(l[i][j])
print(l)
ch=0
for i in range(len(l)):
    if (l[i][1]-l[i][0])>1:
        ch+=1
    else:
        pass
print(ch)

    
