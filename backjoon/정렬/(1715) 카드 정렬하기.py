"""
카드정렬하기
https://www.acmicpc.net/problem/1715

계속 정렬을 해나갸한다.

1 2 3 4 5

3 + 6 + 9 + 15 = 33

-> 3 (1+2)
-> 6 (3+3)
-> 9 (4+5)
-> 15 (6+9)

-> 3
-> 6
-> 10
-> 15


10 20 40

-> 30 (10 + 20)
-> 70 (30 + 40)

"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = []
result = 0
for _ in range(n):
    heapq.heappush(data, int(input()))


while len(data) != 1:
    first = heapq.heappop(data)
    second = heapq.heappop(data)
    sum_data = first+second
    result += sum_data

    heapq.heappush(data, sum_data)
print(result)



