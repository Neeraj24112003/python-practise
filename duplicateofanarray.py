nums = list(map(int,input().split()))
dupli = []
for i in nums:
      if i not in dupli:
            dupli.append(i)
print(len(dupli))
