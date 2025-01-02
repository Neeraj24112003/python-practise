nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
q = []
for i in range(len(sorted_nums)):
      square = sorted_nums[i]*sorted_nums[i]
      q.append(square)
print(q)
