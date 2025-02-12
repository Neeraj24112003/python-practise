t = int(input())
for i in range(t):
    n,x,k = map(int,input().split())
    
    if (k//x)>=n:
       print(n)
        
    else:
        print(k//x)