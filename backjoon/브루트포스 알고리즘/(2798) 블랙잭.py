"""
블랙잭
https://www.acmicpc.net/problem/2798

"""

n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

sum = 0
max_sum = 0
for i in range(len(data)-2):

    for j in range(i+1,len(data)-1):

        for k in range(j+1, len(data)):

            sum = data[i] + data[j] + data[k]
            if sum <= m and max_sum < sum:
                max_sum = sum

            if sum > m:
                break

print(max_sum)