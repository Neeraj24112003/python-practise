t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    if(a<=b):
        if(b-a<=c):
            print("Yes")
        else:
            print("No")
    else:
        if(a-b<=d):
            print("Yes")
        else:
            print("No")
    