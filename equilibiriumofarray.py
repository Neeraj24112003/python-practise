
x = list(map(int, input().split()))
sorted_arr = sorted(set(x))
rank_map = {}
rank = 1
for value in sorted_arr:
    rank_map[value] = rank
    rank += 1
ranked_arr = [rank_map[element] for element in x]
print(ranked_arr)
