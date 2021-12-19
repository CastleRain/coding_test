"""
이코테 p312

크게 두가지 경우로 볼 수 있다.
쉽게 코딩이 되는 경우와 약간 돌아가지만 시간 복잡도가 줄 수있는 방법이다.

첫번째는 문자열을 받아오며 +된 값과 *의 값을 확인하며 최댓값을 리턴해주는것이다.

두번째는 처음을 제외한 나머지는 곱셈을 하되 0을 받아올 시 덧셈을 하는것이다.

-> 진행을 하고나서보니 어짜피 for문으로 진행하는것은 같아 시간복잡도는 같다. 연산 하나 차이라 속도 차이도 매우 적을것이다.

예제)
1) 입력
02984
1) 출력
576

2) 입력
567
2) 출력
210
"""

# 첫번째

# n = input()
#
# first = int(n[0])
#
# for i in range(1, len(n)):
#     # 다음값 받아온 값을 second에 저장
#     second = int(n[i])
#
#     plus = first + second
#     mul = first * second
#
#     first = max(plus, mul)
#
# print(first)

# 두번째

# n = input()
#
# first = int(n[0])
#
# for i in range(1, len(n)):
#
#     if first == 0 or n[i] == "0":
#         first += int(n[i])
#     else:
#         first *= int(n[i])
#
# print(first)