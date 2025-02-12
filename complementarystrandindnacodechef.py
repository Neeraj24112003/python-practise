t = int(input())
for i in range(t):
    n=int(input())
    d=input()
    s=""
    for j in d:
        if j=='A':
            s+='T'
        elif j=='T':
            s+='A'
        elif j=='C':
            s+='G'
        else:
            s+='C'
    print(s)
    