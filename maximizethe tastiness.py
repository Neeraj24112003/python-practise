t = int(input())
for i in range(t):
        a,b,c,d = map(int,input().split())
        z = max(a,b)
        y = max(c,d)
        print(z+y)
