t = int(input())
for i in range(t):
    x, y = map(int,input().split())
    if x < y:
        print(y-x)
    elif x>y:
        print(x-y)
    else:
        print(0)
    