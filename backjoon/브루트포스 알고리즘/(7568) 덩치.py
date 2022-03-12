"""
https://www.acmicpc.net/problem/7568
덩치

sort해서 키, 몸무게가 같은 등수인 것은 고정 나머지는 제일 높은 순위로 고정


"""

n = int(input())

weight, height = [], []
rank = [0] * (n)
for i in range(n):

    w, h = map(int, input().split())
    weight.append([w, i])
    height.append([h, i])

weight_sort = sorted(weight, key = lambda x: -x[0])
height_sort = sorted(height, key = lambda x: -x[0])

rank_point = 1
cnt = 0
for k in range(n-1):
    if weight_sort[k][0] > weight_sort[k+1][0] and height_sort[k][0] > height_sort[k+1][0]:
        rank_point += cnt
        cnt = 0
        rank[k] = rank_point
        rank_point +=1
        
        if k == n-2:
            rank_point += cnt
            cnt = 0
            rank[k+1] = rank_point
            rank_point +=1
    else:
        rank[k] = rank_point
        cnt += 1

        if k == n-2:
            rank[k] = rank_point

for l in range(n):
    print(rank[l], end = " ")






# n = int(input())

# weight, height = [], []
# rank = [0] * (n+1)
# for i in range(n):

#     w, h = map(int, input().split())
#     weight.append([w, i])
#     height.append([h, i])

# weight_sort = sorted(weight, key = lambda x: -x[0])
# height_sort = sorted(height, key = lambda x: -x[0])


# # 같은 위치에 같은 사람이 위치하면 해당 위치가 순위이다.

# rank_point = 1
# cnt = 0
# error = 0
# error_stack = []
# for k in range(n):
#     if weight_sort[k][1] == height_sort[k][1]:

#         if error != 0:
#             rank[weight_sort[k][1]] = rank_point
#             cnt += 1
#         else:
#             rank_point += cnt
#             cnt = 0
#             rank[weight_sort[k][1]] = rank_point
#             rank_point+=1
#     else:
#         if error == 0:

#             error +=1
#             error_stack.append(weight_sort[k][1])
#             rank[weight_sort[k][1]] = rank_point
#             cnt+= 1
#         else:
#             if error_stack[0] == height_sort[k][1]:
#                 error -= 1
#                 error_stack.pop(0)
#                 rank[weight_sort[k][1]] = rank_point
#                 cnt+= 1

#             else:
#                 error += 1
#                 error_stack.append(weight_sort[k][1])
#                 rank[weight_sort[k][1]] = rank_point
#                 cnt+= 1


# for l in range(n):
#     print(rank[l], end = " ")



# rank = [1] * n

# for _ in range(n):
#     data.append(list(map(int, input().split())))



# for i in range(n):

#     first_data = data[i]


#     for j in range(n):
#         if i != j:
#             second_data = data[j]

#             rank_data = rank[i]


#             if (first_data[0] > second_data[0]) and (first_data[1] > second_data[0]):
#                 rank[j] += 1
#             elif (first_data[0] < second_data[0]) and (first_data[1] < second_data[1]):
#                 rank[i] += 1



# print(rank)
