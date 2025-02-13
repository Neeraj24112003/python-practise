t = int(input())
for i in range(t):
    a,x,b,y = map(int,input().split())
    speed1 = a/x
    speed2 = b/y
    if speed1==speed2:
        print("Equal")
    elif speed1>speed2:
        print("Alice")
    else:
        print("Bob")