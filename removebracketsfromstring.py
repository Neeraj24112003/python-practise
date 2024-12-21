x = input()
brackets = ["(",")","[","]","{","}"]
alp = ""
bra = ""
for i in x:
      if i in brackets:
            bra+=i
      else:
            alp+=i
print(alp)
