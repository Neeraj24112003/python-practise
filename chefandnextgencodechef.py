t = int(input())
for i in range(t):
    a,b,x,y = list(map(int,input().split()))
    total_capable = a*b
    moon_capable = x*y
    if moon_capable>=total_capable:
        print("Yes")
    else:
        print("No")
