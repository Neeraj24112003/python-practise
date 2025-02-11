t = int(input())
for i in range(t):
    x,y,z = list(map(int,input().split()))
    total_students = x*y
    per = (z/total_students)*100
    if per > 50:
        print("YES")
    else:
        print("NO")
