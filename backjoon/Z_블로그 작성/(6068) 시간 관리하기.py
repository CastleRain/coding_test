"""
https://www.acmicpc.net/problem/6068

N개의 해야 할 일에 숫자

끝내야 하는 것 T
끝내야하는 시간 S
시작 t = 0
최대한 늦게 일어나고 싶다

T, S를 입력으로 받는다.
T = 걸리는 시간
S = 끝내야하는 시간

s-t가 되면 무조건 거기에선 시작해야하는 시간이 나온다.
2   -> 3시간
6   -> 8시간
15  -> 5시간
15  -> 1시간

최소한 2시에는 일어나야한다. ==> 더 빨리 일어날 수 있다. 근데 0시 이하가 되면 -1을 출력해주면된다.
여기에서 문제점은 그 시간에 일어났을때 나머지 들을 진행할 수 있는가?이다.

1. s-t의 min값을 가져온다. (해당값을 첫 스타트로 생각한다.) s-t를 한 값을 start_time이라고 하자.
2. s-t를 기준으로 정렬을 한다
3. start_time + s가 t보다 작으면 pass (현재 시간 = now_time으로 지정해서 해당 값을 키운다.)
    - 크면 해당 값만큼 start_time을 뺴주고 만약 0보다 작다면 -1을 출력해주고 break해준다.
     ++ 만약 0보다 크다면 now_time += s값이 되게된다.

4. 비교문 + 반복문(1000)이므로 충분히 가능할 것으로 판단

"""





import sys

input = sys.stdin.readline


def solution(data):
    total_time = 0
    limit_time = 1e9
    for t, s in data:
        total_time += t
        if total_time > s:
            return -1
        limit_time = min(limit_time, s-total_time)
    return limit_time
    

if __name__ == "__main__":

    n = int(input())

    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    data.sort(key = lambda x:x[1]) 
    print(solution(data))


# -1이 되도록
    # 3
    # 2 6   4
    # 2 4   2
    # 1 4   3
    # -> -1

# 40정도 남겨놓기?
    # 3
    # 40 100
    # 30 90
    # 40 50
    # 60
    # 60
    # 
