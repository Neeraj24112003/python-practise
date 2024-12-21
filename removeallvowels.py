x = input()
vowels = ['a','e','i','o','u']
v = ""
c = ""
for i in x:
      if i in vowels:
            v+=i
      else:
            c+=i


print(v,c)
