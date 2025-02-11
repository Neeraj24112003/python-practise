t = int(input())
for i in range(t):
    n = int(input())
    total_income = 50*n
    sugarcane = (20/100)*total_income
    salt = (20/100)*total_income
    shoprent = (30/100)*total_income
    profit = total_income - (sugarcane+salt+shoprent)
    print(int(profit))
