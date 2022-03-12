"""
https://www.acmicpc.net/problem/9663


한 행에 하나씩만 들어설 수 있으므로 열의 위치를 리스트에 기록해주자.

1. 같은 열에 있으면 안된다.
2. 위의 행부터 백트래킹을 해올 예정이므로 오른쪽 대각선, 왼쪽 대각선에 값이 있는지만 확인하면된다.(위쪽을 계속 화인하면된다.)
    
"""


def solution(n):
    global cnt
    
    # 전체 다 돌았는 경우
    if len(data) == n:
        cnt += 1
        return
    
    # 비교를 해나가면서 진행

    for i in range(n):
        
        if len(data) == 0:
            data.append(i)
        
        # 같은 열인지, 대각선인지 확인 (만약 있으면 다음 값으로 넘어간다.)
        else:
            for j in data:
                # 같은 열 확인
                if j == i:
                    break
                else:
                    # 대각선 확인 행 : len(data) + 1, 열 : i
                    for k in range(len(data)):
                        if len(data) - k






if __name__ == "__main__":
    cnt = 0
    n = int(input())
    data = []
    solution(n, data)