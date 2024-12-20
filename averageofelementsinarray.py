s = list(map(int, input().split()))
su = 0
for i in range(len(s)):
      su= su + s[i]
avg = su/len(s)
print(avg)
