x = input()
vowels = ['a','e','i','o','u']
space = [" "]
v_count = 0
c_count = 0
s_count = 0
for i in x:
      if i in vowels:
            v_count+=1
      elif i in space:
            s_count+=1
      else:
            c_count+=1

print(v_count,c_count,s_count)
