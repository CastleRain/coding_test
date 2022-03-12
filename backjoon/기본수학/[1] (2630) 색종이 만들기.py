"""
https://www.acmicpc.net/problem/2630

한줄을 읽었을 때 데이터가 다 같으면 안나눠도 되는 상황이다.


# https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python
참고해서 풀었음

풀이방법은 비슷하나 가는 과정에서 난 막힘.


"""
import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

result = []


def solution(x, y, n):
    
    color = data[x][y] # 현재 색을 확인

    for i in range(x, n+x): # 처음 시작부터 범위를 벋어나기 전까지 진행을 하도록 더해준다.
        for j in range(y, n+y):
            if color != data[i][j]:
                # 4개의 공간을 돌아다닌다.
                solution(x, y, n//2) 
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        result.append(0)
    else:
        result.append(1)


    return 0

solution (0, 0, n)
print(result.count(0))
print(result.count(1))









# import sys

# input = sys.stdin.readline

# # cnt : 사각형 갯수
# white_cnt, blue_cnt  = 0, 0

# # num : 필요한 사각형 갯수
# white_num, blue_num = 0, 0


# n = int(input())

# # 이진수로 변환
# def make_two(num):
#     result = []
#     while num > 0:
#         if num % 2 == 1:
#             result.append(1)
#         else:
#             result.append(0)
#         num //= 2
#     print(result[::-1])
        



# for _ in range(n):
#     data = list(map(int, input().split()))

#     for i, d in enumerate(data):
#         if i != 0:




