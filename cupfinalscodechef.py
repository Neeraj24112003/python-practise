t = int(input())
for i in range(t):
    x,y,d = map(int,input().split())
    if x>=y:
        z = x-y
    else:
        z = y-x
    if z <= d:
        print("YES")
    else:
        print("NO")