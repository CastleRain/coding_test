"""
ATM

5
3 1 4 3 2

-> 32

"""


""" 
정렬해서 가져오면 되는 문제같다.

"""


input()

data = list(map(int, input().split()))

# data.sort()
# result = 0
# sum = 0
#
# for i in data:
#     sum += i
#     result += sum
# print(result)

data.sort(reverse=True)
result = 0

for i, j in enumerate(data):
    result += j*(i+1)

print(result)
