n=int(input())
ch=0

if (n%4)==0:
    ch+=1

if (n%7)==0:
    ch+=1

if (n%44)==0:
    ch+=1

if (n%77)==0:
    ch+=1

if (n%47)==0:
    ch+=1

if (n%74)==0:
    ch+=1

if (n%444)==0:
    ch+=1

if (n%777)==0:
    ch+=1

if (n%447)==0:
    ch+=1

if (n%474)==0:
    ch+=1

if (n%744)==0:
    ch+=1

if (n%774)==0:
    ch+=1

if (n%747)==0:
    ch+=1

if (n%477)==0:
    ch+=1

if ch>0:
    print("YES")
else:
    print("NO")

    
