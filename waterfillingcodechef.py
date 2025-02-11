t= int(input())
for i in range(t):
    b1,b2,b3 = list(map(int,input().split()))
    k=[b1,b2,b3].count(0)
    if k>=2:
        print('Water filling time')
    else:
        print("Not now")
