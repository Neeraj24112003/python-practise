arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr2_set = {element for element in arr2}
subset = True
for element in arr1:
    if element not in arr2_set:
        subset = False
        break
if subset:
    print("arr1 is a subset of arr2")
else:
    print("arr1 is not a subset of arr2")
