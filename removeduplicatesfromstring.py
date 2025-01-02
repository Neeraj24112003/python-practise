s = input()
dupli = ""
nondupli = ""
for i in s:
      if i not in dupli:
            dupli+=i
      else:
            nondupli+=i
print(dupli)
print(nondupli)
