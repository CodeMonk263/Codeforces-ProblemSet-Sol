n=input()
l=list(n)
ch1,ch2=0,0

for i in range(len(l)):
    if 90>=ord(l[i])>=65:
        ch1+=1
for i in range(1,len(l)):
    if 90>=ord(l[i])>=65:
        ch2+=1
        
if ch1==(len(l)):
    for i in range(len(l)):
        l[i]=l[i].lower()
elif ch2==(len(l)-1) and (l[0].islower()==True):
    l[0]=l[0].upper()
    for i in range(1,len(l)):
        l[i]=l[i].lower()
else:
    pass

n=''.join(l)    
print (n)







