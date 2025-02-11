t = int(input())
for i in range(t):
    r1,r2,r3,r4 = list(map(int,input().split()))
    k=[r1,r2,r3,r4].count(1)
    if k == 0:
        print("IN")
    else:
        print("OUT")
