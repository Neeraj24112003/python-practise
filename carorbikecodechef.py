t = int(input())
for i in range(t):
    x,y = list(map(int,input().split()))
    if x>y:
        print("Car")
    elif x<y:
         print("Bike")
    else:
        print("same")
