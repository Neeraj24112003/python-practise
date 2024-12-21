x = input()
y = x.split()
print(y)
for i in y:
      z = str(i[0]).upper() + str(i[1:-1]) + str(i[-1]).upper()
      print(z)
