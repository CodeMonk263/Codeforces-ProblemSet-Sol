s=int(input())
ls=[]
ch=0
x=True

while(s>0):
    temp=s%10
    ls.append(temp)
    s//=10

ls.reverse()


for i in range(len(ls)):
    if ((ls[i]==4) or (ls[i]==7)):
        ch+=1

lch=[]
while(ch>0):
    temp=ch%10
    lch.append(temp)
    ch//=10

if lch==[]:
    lch.append(0)
    
lch.reverse()

for j in range(len(lch)):
    if ((lch[j]==4) or (lch[j]==7)):
        x=True
    else:
        x=False

if x==False:
    print ('NO')
else:
    print ('YES')
