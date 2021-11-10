"""
덩치

"""

n = int(input())

data = []

rank = [1] * n

for _ in range(n):
    data.append(list(map(int, input().split())))



for i in range(n):

    first_data = data[i]


    for j in range(n):
        if i != j:
            second_data = data[j]

            rank_data = rank[i]


            if (first_data[0] > second_data[0]) and (first_data[1] > second_data[0]):
                rank[j] += 1
            elif (first_data[0] < second_data[0]) and (first_data[1] < second_data[1]):
                rank[i] += 1



print(rank)
