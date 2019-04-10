n=int(input(""))
x=input("")
ch=0
for i in range(len(x)):
    if i==0:
        pass
    else:
        if x[i]==x[i-1]:
            ch+=1
print(ch)
