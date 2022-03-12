"""
https://www.acmicpc.net/problem/15663


N, M이 주어진다

백트래킹이지만 중복되는 숫자는 하나씩만 나오게 해야한다.

위에서 선택이 안된 숫자는 
1 1 2 3 3 3

1 2 3
1 3 
3

0 1 2 3 4 5 (숫자)
0 2 1 3 2 2 (갯수)

여기에서 하나씩 빼오는 방식을 택할 수 있을까?
M, N이 갯수가 적으므로 다 진행한 후 set을 할까?
"""

def solution(data, m):
    global result
    
    if len(answer) == m:
        result.append("".join(map(str, answer)))
        return

    for i in data:
        answer.append(i)
        solution(data, m)
        answer.pop()

    return result





if __name__ == "__main__":
    result = []
    answer = []
    n, m = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    d = sorted(list(set(solution(data, m))))
    for i in d:
        print(" ".join(i))

