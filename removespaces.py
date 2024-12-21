x = input()
s = [" "]
st = ""
nst = ""
for i in x:
      if i in s:
            nst+=i
      else:
            st+=i


print(st,nst)
