x = input()
y = x.split()
print(y)
for i in y:
      z = str(i[0]).lower() + str(i[1:-1]).upper() + str(i[-1]).lower()
      print(z)
