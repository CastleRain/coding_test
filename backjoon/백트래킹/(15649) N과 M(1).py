"""
https://www.acmicpc.net/problem/15649

백트래킹 공부

https://blog.encrypted.gg/732
여기보고 공부시작

https://wlstyql.tistory.com/56
이곳에서 마무리 침


만약 depth가 원하는 값(m)이면 값을 다 출력하고 빠져나온다.

depth가 원하는 값이 아니면 (무조건 작음) 

n만큼 돌면서 현재 방문을 했는 값인지 확인 방문을 안했다면 list에 저장
그리고 다시 함수를 재시작

그 함수는 depth가 끝날때 까지 돌것이므로 함수가 끝나면 list 첫번째값 삭제, 그리고 해당 값 방문 안한것으로 바꾸기

"""

n, m = map(int, input().split())

visited = [False] * n
result = []


# def n_m(visited, result, n, m):

#     if len(result) == m:

#         print(' '.join(result))
#         return

#     for i in range(0, n):

#         if not visited[i]:

#             result.append(str(i+1))
#             visited[i] = True
#             n_m(visited, result, n , m)
#             visited[i] = False
#             result.pop()

# n_m(visited, result, n, m)

def n_m(result):

    if len(result) == m:

        print(' '.join(result))
        return

    for i in range(0, n):

        if not visited[i]:

            result.append(str(i+1))
            visited[i] = True
            n_m(result)
            visited[i] = False
            result.pop()

n_m(result)