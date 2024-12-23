x = input()
duplicates = ""
nonduplicates = ""
for i in x:
      if i not in nonduplicates:
            nonduplicates+=i
      else:
            duplicates+=i
print(nonduplicates)
print(duplicates)
