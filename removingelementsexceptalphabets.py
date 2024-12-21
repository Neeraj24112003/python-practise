x = input()
num = ['1','2','3','4','5','6','7','8','9','0']
sp = [" "]
spc = ['!',"@","#"]
n = ""
s = ""
sc = ""
alp= ""
for i in x:
      if i in num:
            n+=i
      elif i in sp:
            s+=i
      elif i in spc:
            sc+=i
      else:
            alp+=i
print(alp)
