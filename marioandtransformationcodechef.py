t = int(input())
for i in range(t):
    x=int(input())
    if x%3==0:
        print("normal")
    elif x%3==2:
        print("small")
    else:
        print("huge")