t=int(input())
for i in range(t):
    z=list(map(int,input().split()))
    a=max(z)
    z.remove(max(z))
    b=sum(z)
    if(a>b):
        print("YES")
    else:
        print("NO")
