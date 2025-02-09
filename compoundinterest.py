p = float(input())
t = float(input())
r = float(input())

amount = p*((1+r/100)**t)

ci = amount - p
print(ci)
