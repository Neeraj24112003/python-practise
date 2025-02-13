t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    if a+c and b+d == 180:
        print("Yes")
    else:
        print("No")