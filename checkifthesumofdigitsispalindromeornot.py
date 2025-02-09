n = int(input())
z = str(n)
sum = 0
for i in z:
      sum += int(i)
print(sum)
if str(sum) == str(sum)[::-1]:
      print("True")
else:
      print("False")
