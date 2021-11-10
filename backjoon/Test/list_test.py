n = 6

## 5,5 -> 4,5 -> 4,4 -> 3,5

for a in range(n-1, -1, -1):


    for b in range(a, a, -1):


        print(f"{b},{a}")