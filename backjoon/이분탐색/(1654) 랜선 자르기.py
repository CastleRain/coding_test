"""
랜선 자르기

"""

k, n = map(int, input().split())

data = []
for i in range(k):
    data.append(int(input()))

# data의 최대값 저장
max_data = max(data)
first_data = 1


# n의 갯수가 나오는 최저값구하기
while True:
    result = 0

    if max_data < first_data:
        break

    mid = (max_data + first_data) // 2

    for j in data:
        if mid == 0:
            break
        result += j//mid

    # 만들어진 수가 원하는 값보다 작은 경우 mid를 더 줄여 값을 늘려야한다.
    if result < n:
        max_data = mid-1
    # 만들어진 수가 원하는 보다 큰 경우 mid를 늘려가보며 더 큰값이 나올수 있는지 확인한다.
    else:
        # 값 저장을 위해 lan_len을 만들어놓는다.
        lan_len = mid
        first_data = mid + 1

print(lan_len)
