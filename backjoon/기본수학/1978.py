"""
소수찾기

"""

n = int(input())

data = list(map(int, input().split()))

result = []

for i in data:
    cnt = 0
    if i != 1:

        for j in range(2, i):
            if i%j == 0:
                cnt+=1
        if cnt == 0:
            result.append(i)

print(len(result))



