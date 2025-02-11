t = int(input())
for i in range(t):
    x,y = list(map(int, input().split()))

    b= x*y
    if b >= 100:
        print((b//100))
    else:
        print(0)
