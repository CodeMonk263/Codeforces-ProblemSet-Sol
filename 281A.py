s=input("")
l=list(s)
if ord(l[0])>=97 and ord(l[0])<=122:
    l[0]=l[0].upper()

print(''.join(l))
