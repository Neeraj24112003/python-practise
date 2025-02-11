t = int(input())
for i in range(t):
    x,a,b = list(map(int,input().split()))
    c = a + (b*2)
    if c >= x:
        print("Qualify")
    else:
        print("NotQualify")