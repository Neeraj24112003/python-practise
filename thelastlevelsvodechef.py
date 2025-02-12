t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    if x%3==0:
        print((x*y)+((x//3)-1)*z)
    else:
        print((x*y)+((x//3)*z))