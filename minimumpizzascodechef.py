import math
t = int(input())
for i in range(t):
    n,x = list(map(int,input().split()))
    print(math.ceil((n*x)/4))
