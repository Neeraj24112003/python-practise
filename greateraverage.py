n = int(input())
for i in range(n):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    avg = (a+b)/2
    if avg > c:
        print("YES")
    else:
        print("NO")
