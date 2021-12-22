"""
dfs에 대해 생각을 해보자.

1. 처음 시작하는 지점에서 제일 작은 숫자를 스택에 집어넣는다. (출력한다.)
2. 만약 방문하지 않은 노드라면 스택에 넣고 다시 1을 반복한다.
3. 더 방문할 곳이 없다면 스택에서 뺸다.
4. 스택에 남은 것이 없다면 빠져나온다.


"""








# 내가 만든 코드


# def dfs(graph, first, visited):
    
#     # 첫번째 데이터 방문처리
#     if visited[first] == False:
#         visited[first] = True
#         print(first, end = ' ')

#     # i에는 그 다음 데이터가 들어오게 된다.
#     for i in graph[first]:

#         # 현재 방문하지 않았는 데이터라면
#         if visited[i] == False:

#             visited[i] = True
#             print(i, end = ' ')

#             dfs(graph, i, visited)


def dfs(graph, v, visited):

    visited[v] = True
    print(v, end= ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

dfs(graph, 1, visited)