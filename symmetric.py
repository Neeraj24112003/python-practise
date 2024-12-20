x = list(map(int, input().split()))
pairs = []

for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] == x[j] and x[i] not in pairs:
            pairs.append(x[i])

print(pairs)
