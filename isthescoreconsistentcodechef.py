t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    if(c>=a and d>=b):
        print("Possible")
    else:
        print("Impossible")
