t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    d = []
    d.append(a)
    d.append(b)
    d.append(c)
    f = sorted(d)
    print(f[1])