t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if(n<=m):
        print(n)
    else:
        print(n+(n-m))
