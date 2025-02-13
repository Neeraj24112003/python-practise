t = int(input())
for i in range(t):
    a,b,x,y = map(int,input().split())
    chef = a/x
    chefina = b/y
    if chef<chefina: 
        print("chef")
    elif chef>chefina: 
        print("chefina")
    else: 
        print("both")