l1=[]
for k in range(5):
    x=input()
    l1.append(x.split())
for i in range(5):
    for j in range(5):
        lt=l1[i]
        if lt[j]=='1':
            remi=i
            remj=j
moves=abs(2-remi)+abs(2-remj)
print(moves)
