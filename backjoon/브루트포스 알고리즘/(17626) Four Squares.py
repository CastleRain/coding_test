"""
https://www.acmicpc.net/problem/17626

4개 이하의 제곱숭의 합으로 모두 다 만들수있다.

n = 50000이하다.

num <= 223이어야한다.

num 224** 2 = 50176

"""


# dp = []

# count = 0
# for i in range(1, 224):

#     dp.append(i**2)

# n = int(input())

# result = 10


# # 하나로 완성
# if n in dp:
#     print(1)

# else:
    
#     # 두개로 완성
#     for i in range(int(n**0.5), 0, -1):
#         if dp[i] == n:
#             result = 1
#             break
#         if dp[i][1] < n:
#             break
        
#         for j in range(i, 0, -1):
#             if dp[i][0] + dp[j][0] == n:
#                 result = min(result, 2)
#             if dp[j][1] + dp[i][0] < n:
#                 break
        



n = int(input())

first_dp = [0]
for i in range(1, 224):
    first_dp.append(i**2)
    if i**2 > n:
        break

result = 4

if n in first_dp:
    result = 1
else:
    for i in range(int(n**0.5), 0, -1):
        for j in range(i, 0, -1):
            if first_dp[i] + first_dp[j] == n:
                result = 2
                break      
            for k in range(j, 0, -1):
                if first_dp[i] + first_dp[j] + first_dp[k] == n:
                    result = min(result, 3)
   
print(result)


# dp = [[] * _ for _ in range(224)]

# count = 0
# for i in range(1, 224):
#     count += i ** 2
#     dp[i] = [i**2, count]

# n = int(input())

# result = 10


# for i in range(int(n**0.5), 0, -1):
#     if dp[i][0] == n:
#         result = 1
#         break
#     if dp[i][1] < n:
#         break
    
#     for j in range(i, 0, -1):
#         if dp[i][0] + dp[j][0] == n:
#             result = min(result, 2)
#         if dp[j][1] + dp[i][0] < n:
#             break
        
#         for k in range(j, 0, -1):
#             if dp[i][0] + dp[j][0] + dp[k][0] == n:
#                 result = min(result, 3)  
#             if dp[k][1] + dp[j][0] + dp[i][0] < n:
#                 break      
            
#             for m in range(k, 0, -1):
#                 if dp[i][0] + dp[j][0] + dp[k][0] + dp[m][0] == n:
#                     result = min(result, 4) 
#                 if dp[m][1] + dp[j][0] + dp[i][0]+dp[k][0] < n:
#                     break  
# print(result)

