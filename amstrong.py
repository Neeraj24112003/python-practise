number = int(input())
n = len(str(number))
total_sum = 0

for i in str(number):
    total_sum += int(i) ** n

if total_sum == number:
    print("True")
else:
    print("False")
