t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if x%n==0:
        print("yes")
    else:
        print("no")