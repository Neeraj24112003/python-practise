s = list(map(int, input().split()))
for i in range(len(s)):
      if len(s) % 2 == 0:
            a = s[(i)//2]-1
            b = s[i//2]
            median = (a+b)/2
      else:
            median = s[(i)//2]
print(median)
