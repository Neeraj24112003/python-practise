x = list(map(int,input().split()))
sorted_arr = []
for i in range(len(x)):
      sorted_arr.append(x[i])
y = x.sort()
for i in sorted_arr:
      y = x.index(i)
      print(y)
