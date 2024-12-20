arr = list(map(int, input().split()))
frequency = {}
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))
print(sorted_arr)
