t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a+b<11:
        print("-1")
    else:
        print(21-(a+b))