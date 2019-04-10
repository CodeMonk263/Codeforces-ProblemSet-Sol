s=input()
l=list(s)
sch=0
for i in range(len(l)):
    pch=0
    for j in range(0,i):
        if l[i]==l[j]:
            pch+=1
        else:
            pass
    if pch>0:
        pass
    else:
        sch+=1
        
if sch%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

    
    
