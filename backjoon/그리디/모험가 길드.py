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

1. 받아온 값을 정렬한다.
2. pop을 통해 제일 마지막 공포도를 leader로 저장한다.
3. 현재 leader도 포함되어있으므로 leader - 1만큼 팀에 들어갈수 있다. 만약 data의 값이 적다면 pop 에러가 뜨므로 반복문을 나가주자.
4. team_count를 증가하면서 계속 진행한다.
5. 값을 출력해준다.


"""
import sys

# 많이 입력될 경우 시간제한 걸릴수도 있으므로 readline사용
input = sys.stdin.readline


n = int(input())

data = list(map(int, input().split()))

data.sort()

team_count = 0

while True:
    team_leader = data.pop()-1
    team_count += 1
    if len(data) <= team_leader:
        break
    for _ in range(team_leader):
        data.pop()

print(team_count)