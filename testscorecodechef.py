t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    if y%x==0 and y <= n*x:
        print("yes")
    else:
        print("No")