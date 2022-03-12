"""
https://www.acmicpc.net/problem/15656


"""

n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

result = []


def n_m(result):

    if len(result) == m:
        for k in result:
            print(str(k), end=" ")
        print()
        return

    # for i in range(start, n):
    #     result.append(data[i])
    #     n_m(i, result)
    #     result.pop()
    for i in range(n):
        result.append(data[i])
        n_m(result)
        result.pop()

n_m(result)