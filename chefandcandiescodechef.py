t = int(input())
for i in range(t):
    n,x = list(map(int,input().split()))
    if n > x:
        print((n - x + 3) // 4)
    else:
        print(0)
