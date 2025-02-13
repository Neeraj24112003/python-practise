t = int(input())
for i in range(t):
    x,n = map(int,input().split())
    if(n//100>=x):
        if(n%100 > 0):
            print(n//100 - x + 1)
        else:
            print(n//100 - x)
    else:
        print(0)