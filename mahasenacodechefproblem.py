n = int(input())
odd_count = 0
even_count = 0

a = list(map(int,input().split()))
for j in a:
      if j%2 == 0:
            even_count += 1
      else:
            odd_count +=1
if even_count>odd_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
