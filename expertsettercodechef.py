t = int(input())
for i in range(t):
    x,y = list(map(int,input().split()))
    per = (y/x)*100
    if per >= 50:
        print("Yes")
    else:
        print("No")
