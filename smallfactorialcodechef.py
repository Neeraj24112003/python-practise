t = int(input())
for i in range(t):
    n = int(input())
    a = 1
    for j in range(1,n+1):
        a*=j
    
    print(a)