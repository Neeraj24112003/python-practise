t = int(input())
for i in range(t):
    w,x,y,z = map(int,input().split())
    if w==x or w==y or w==z:
        print("yes")
    elif w==(x+z) or w==(x+y) or w==(y+z) or w==(x+y+z):
        print("yes")
    else:
        print("no")
    