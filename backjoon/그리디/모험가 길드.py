"""
이코테 p311

공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야한다

처음 N(사람수)이 주어지며 다음 공포도가 주어진다

이때 만들어 질수 있는 최대값을 출력하시오.

1 <= N <= 100000

5
2 3 1 2 2

-> 2

(1,2,3 / 2,2)
"""


"""
내 풀이 과정

1. 사람의 공포도를 리스트로 받아온 뒤 정렬

2. 제일 큰 공포도만큼 팀 생성 (pop을 이용하여 제일 뒤에서 부터 하나씩 가져옴)

3. 팀 생성이 끝나면 그 다음 공포도 만큼 생성

4. 만약 list의 길이가 0이되면 반복문 빠져나오기

 자세한건  https://castlerain.tistory.com/17?category=904402 참고

"""
# import sys
#
# # 많이 입력될 경우 시간제한 걸릴수도 있으므로 readline사용
# input = sys.stdin.readline
#
# # n = 몇개를 입력받을것인지 확인 (사실 이곳에선 딱히 필요없는 코드여서 input()하고 넘어가도 괜찮다.
# n = int(input())
#
# # list 형식으로 받아오면서 띄어쓰기를 기준으로 나눠주자
# data = list(map(int, input().split()))
#
# # 받아온 데이터를 정렬한다.
# data.sort()
#
# # team_count = 팀이 몇개인지 알려주는 값
# team_count = 0
#
# # data의 길이가 team_leader보다 낮을 때 종료한다.
# while True:
#
#     # team_leader는 data에서 제일 마지막 숫자를 받아오면서 그 팀은 팀장을 포함한 값이 있어야 하므로 -1을 해주었다.
#     team_leader = data.pop()-1
#
#     # 팀을 하나 증가시킨다.
#     team_count += 1
#
#     # team_leader보다 data가 적다면 팀의 구성이 완료된것이므로 반복문을 빠져나가자.
#     # 만약 <이 된다면 팀의 구성은 완료되지만 위의 data.pop에서 오류가 뜨게된다. try catch를 쓰게되면 상관없지만 그렇게까지 들어가고 싶진않다.
#     if len(data) <= team_leader:
#         break
#
#     # team_leader만큼 pop을 통해 데이터를 없애주자.
#     for _ in range(team_leader):
#         data.pop()
#
# # 마지막으로 팀 갯수를 보여주면된다.
# print(team_count)


"""
책 풀이
"""

# n = int(input())
# data= list(map(int, input().split()))
# data.sort()
#
# result = 0
# count = 0
#
# for i in data:
#     count += 1
#     if count >= i:
#         result +=1
#         count = 0
#
# print(count)

"""
다시 만듬
"""

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# pop이라는것을 그대로 이용하기위해 reverse를 사용하자.
data.sort(reverse=True)

team_count = 0

while True:


    team_leader = data.pop()-1

    # 팀을 하나 증가시킨다.
    team_count += 1

    # team_leader보다 data가 적다면 팀의 구성이 완료된것이므로 반복문을 빠져나가자.
    # 만약 <이 된다면 팀의 구성은 완료되지만 위의 data.pop에서 오류가 뜨게된다. try catch를 쓰게되면 상관없지만 그렇게까지 들어가고 싶진않다.
    if len(data) > team_leader:
        break

    # team_leader만큼 pop을 통해 데이터를 없애주자.
    for _ in range(team_leader):
        data.pop()

# 마지막으로 팀 갯수를 보여주면된다.
print(team_count)