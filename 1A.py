n,m,a=map(int,input().split())

if m%a==0:
 d1=m//a
else:
 d1=m//a+1
 
if n%a==0:
 d2=n//a
else:
 d2=n//a+1
 
print(d1*d2)
