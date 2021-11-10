n = 6

## 5,5 -> 4,5 -> 4,4 -> 3,5 -> 3,4 -> 3,3

for a in range(n-1, -1, -1):


    for b in range(n-1, a-1, -1):


        print(f"{a},{b}")