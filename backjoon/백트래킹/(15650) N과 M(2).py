"""
https://www.acmicpc.net/problem/15650

중복은 제거한다.

백트래킹으로 도는것은 그대로인데 범위가 처음부터가 아니라 빠져나온 다음수부터 진행하도록하면된다

4 2

1

1 2 -> 다시 n_m(1, result)가 들어감 
1 3 -> 다시 n_m(2, result)가 들어감
1 4 -> 다시 n_m(3, result)가 들어감

"""

n, m = map(int, input().split())

visited = [False] * n
result = []


def n_m(i, result):

    if len(result) == m:
        
        
        print(" ".join(result))
        return
    
    for j in range(i, n):

        if not visited[j]:
            visited[j] =True
            result.append(str(j+1))

            n_m(j, result)
            
            visited[j] = False
            result.pop()


n_m(0, result)
