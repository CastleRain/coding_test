"""
수 정렬하기

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N(1 ≤ N ≤ 1,000)

sort함수쓰면 편하게 된다.
"""

data_list = []

for _ in range(int(input())):
    data_list.append(int(input()))

data_list.sort()

for data in data_list:
    print(data)