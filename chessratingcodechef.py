t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    g=0
    while x<y:
        x+=8
        g+=1
    print(g)
        