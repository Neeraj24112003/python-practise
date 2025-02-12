t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    k = n//m
    if n%m != 0:
        print("No")
    elif k%2==0:
        print("Yes")
    else:
        print("No")