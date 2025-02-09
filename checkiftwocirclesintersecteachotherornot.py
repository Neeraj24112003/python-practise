x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
r1 = float(input("Enter r1: "))
r2 = float(input("Enter r2: "))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
if d < r1 + r2:
      print("The circles intersect.")
elif d == r1 + r2:
      print("The circles touch each other.")
elif d == 0 and r1 == r2:
      print("The circles coincide.")
elif d == 0 and r1 != r2:
      print("The circles are concentric.")
elif d > r1 + r2:
      print("The circles are disjoint.")

else:
      print("The circles do not intersect.")
