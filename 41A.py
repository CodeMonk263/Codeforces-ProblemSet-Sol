s=input()
t=input()
sl=list(s)
tl=list(t)
tl.reverse()
ctr=0
if (len(sl)==len(tl)):
    for i in range(len(sl)):
        if tl[i]==sl[i]:
            ctr+=1
        else:
            pass
    
if ctr==len(sl):
    print("YES")
elif len(sl)!=len(tl):
    print("NO")
else:
    print("NO")
