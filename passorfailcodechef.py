t = int(input())
for i in range(t):
    n,x,p = map(int,input().split())
    d = x*3
    remaining = n-x
    total = d + (remaining*(-1))
    if total>=p:
        print("pass")
    else:
        print("Fail")