"""

url : https://www.acmicpc.net/problem/2108
created : 22.01.14
by : CastleRain

선 정렬 후 
산술평균 (first) : round(sum(data)/len(data), 1)
중앙값 (second) : 정렬 후 중간값, 만약 갯수가 짝수인경우 중간의 양옆값의 평균을 내면된다.
최빈값 (thrid) : 가장 많이 나오는 수
범위 (firth) : 오른쪽과 왼쪽값 빼기
"""



from collections import defaultdict

n = int(input())

data = []
data_dic = defaultdict(int)

for _ in range(n):
    i = int(input())
    data.append(i)

    data_dic[i] += 1
data.sort()
data_sort = sorted(data_dic.items(), key = lambda x : (-x[1], x[0]))

print(int(round(sum(data) / len(data),0)))

if len(data) % 2 == 0:
    print(int((data[len(data)//2] + data[len(data)//2 - 1]) / 2) )
else:
    print(data[len(data)//2])

if len(data_sort) > 1:

    if data_sort[0][1] == data_sort[1][1]:
        print(data_sort[1][0])
    else:
        print(data_sort[0][0])
else:
    print(data_sort[0][0])

print(data[-1] - data[0])