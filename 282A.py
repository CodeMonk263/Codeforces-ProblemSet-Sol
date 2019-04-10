n=int(input())
t=[]
x=0
for i in range(n):
    m=str(input())
    t=list(m)
    if t[1]=='+':
        x+=1
    elif t[1]=='-':
        x-=1
    else:
        break

        
print (x)
    
