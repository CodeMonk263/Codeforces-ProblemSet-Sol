s=input()
l=list(s)
x=0

for i in range(len(l)):
    if x==0:
        if l[i]=='h':
            x+=1
        
    elif x==1:
        if l[i]=='e':
            x+=1
        
    elif x==2:
        if l[i]=='l':
            x+=1
        
    elif x==3:
        if l[i]=='l':
            x+=1
        
    elif x==4:
        if l[i]=='o':
            x+=1
    else:
        pass
    if x==5:
        break
    else:
        pass

if x==5:
    print('YES')
else:
    print('NO')
