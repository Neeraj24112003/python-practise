s = input().split()
s = []
for i in range(len(s)):
      if s[i]== '(' or '{' or '[':
            s.append(s[i])
      elif len(s) == 0:
            s.append(s[i])
            break
      else:
            s.pop()
if len(s) > 0:
      print("false")
else:
      print("true")
