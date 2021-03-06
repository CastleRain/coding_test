"""
회의실 배정

문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과
동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는
시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
"""

"""
활동 선택 문제이다.

1. 끝나는 시간을 기점으로 정렬을한다
2. 가장먼저 끝나는 것을 첫번째 지점으로 정한다.
3. 처음 진행된것이 끝난 시점과 그다음 시점을 그대로 가져온다. 계속진행

이 개념이 들어간다. 
sorted(a, key=lambda x:x[1])
"""
n = int(input())

data = []
result = []
start = -1
for _ in range(n):
    data.append(list(map(int, input().split())))
### -> 여기서 틀렸었다.

###sort_data = sorted(data, key=lambda x: x[1])

## 이대로 정렬이 되면 시작시간은 고려가 안되는데 끝나는 시간이 같다면 시작시간이 빠른 순서대로 진행을 하면 좋다.
sort_data = sorted(data, key=lambda x: x[0])
sort_data = sorted(sort_data, key=lambda x: x[1])
# 첫번째 값은 바로 넣는다.
# 다음값부터는 끝난시간과 시작시간이 일치한 혹은 그 이후에 처음 나타나는것을 넣는다.
for i in range(n):
    if start <= sort_data[i][0]:
        result.append(sort_data[i])
        start = sort_data[i][1]

print(len(result))



# 반쯤 맞고 틀림
# n = int(input())
#
# data = []
# result = []
# start = -1
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# sort_data = sorted(data, key=lambda x: x[1])
#
# # 첫번째 값은 바로 넣는다.
# # 다음값부터는 끝난시간과 시작시간이 일치한 혹은 그 이후에 처음 나타나는것을 넣는다.
# for i in range(n):
#     if start <= sort_data[i][0]:
#         result.append(sort_data[i])
#         start = sort_data[i][1]
#
# print(len(result))






