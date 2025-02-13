t = int(input())
for i in range(t):
    k=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in a:
        if j>=10 and j<=60:
            k+=1
            
    print(k)