t = int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=(500-x*2)+(1000-(x+y)*4)
    b=(1000-y*4)+(500-(x+y)*2)
    print(max(a,b))