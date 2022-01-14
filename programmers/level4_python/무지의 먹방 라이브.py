"""
무지의 먹방 라이브
https://programmers.co.kr/learn/courses/30/lessons/42891

"""



"""

내 생각

처음 food_times라는 배열과 k라는 자연수가 주어진다.
이때 food_times에서 0이 되면 그 인덱스는 넘어 다음으로 넘어가야한다.
k만큼 진행하였을 때 어느곳에 위치할 것인가...

사실 정확성으로 보게 되면 k만큼 진행시켜도 2,000,000이므로 0.1초이내에 결과가 나올 것이다.
(food_times는 시간에 영향을 주지 않는다. k만큼 진행하면서 리스트를 계속 변환을 진행하면되므로.)
-> 풀이 1번으로 진행

그런데 효율성 테스트를 보게되면 k가 무려 20,000,000,000,000까지 할수있다고 나온다. 일반적인 for문으로는 진행이 불가하다는 뜻이다.

이 문제의 제일 큰 문제점은 진행이 되면서 food_times가 0이되게되면 그 다음 인덱스로 가야한다는것인데
이를 최대한 줄이는 것이 이 문제의 키포인트라고 생각을 했다.

두번째로 생각한 것은 정렬을 사용하여 제일 작은 숫자만큼은 food_times(0이되는값은 제외)의 크기만큼은 k가 돌 수 있다는것을 알 수 있다.
그리고 set을 이용하여 다음 숫자가 어딘지를 파악할 수 있으며 index를 사용하면 몇개의 데이터가 있는지 알 수 있다. 
(count를 사용하면 O(n)을 사용하므로 이게 더 시간적으로 여유가 있을것이라 판단)
    -> index와 count 둘다 O(n)을 사용하므로 그냥 count로 숫자세는것이 공간복잡도를 안씀
이쯤에서 변수 할당을 진행하면

food_len = 0을 제외한 food_times의 리스트 크기 (실제론 0보다 큰 데이터의 크기를 불러올 예정)
sort_food = food_times 정렬된것 저장
min_index = 0 (이후 min_data count갯수만큼 증가시킬 예정)
min_data = sort_food[0] (제일 작은값 저장)
min_data_count = sort_food.count(min_data) (작은값이 몇개 있는지 확인)



현재 len(food_times) * min_data 




시간복잡도.
정렬 (n logn)

망할 이게 답이아니였다. 우선 처음 답도 안나왔기때문에 정확성부터 틀러버렸다.




"""




# def fcount(food):
#     count_food = food.copy()
#     try:
#         count_food.remove(0)
#     except:
#         pass
#     return len(count_food)
#
#
# def solution(food_times, k):
#     """
#     len(food_times) = food_count라고 하자
#     1. k <= food_count 이면 현재 필드에서 진행된다는것. -> O(n)
#     2. food_count < k이면 food_times의 리스트에 있는 데이터를 다 -1을 한다. O(n)
#     3. 1.반복진행을 하는데 len(food_times)는 0을 제외한 len이 되어야한다. O(n)
#     4. 1.이 될때까지 2,3을 반복한다. O(n^2?)
#     5. 마지막으로 0을 제외한 값만큼 for문을 돌리고 결과값을 받아온다.
#
#
#     """
#     food_count = fcount(food_times)
#     answer = 0
#     while True:
#
#         if k < food_count:
#             count = 0
#             for i in range(len(food_times)):
#                 if food_times[i] != 0:
#                     count += 1
#                 if count == k:
#                     answer = i + 1
#             break
#         else:
#             food_times = [x - 1 for x in food_times]
#
#         k -= food_count
#         food_count = fcount(food_times)
#
#     return answer


# def solution(food_times, k):
#     food_times_copy = food_times.copy()
#     food_len = len(food_times)
#     set_food = list(set(food_times))
#     min_index = 0
#
#     answer = 0
#     test = 0
#     while True:
#         min_data = set_food[min_index]
#         min_data_count = food_times_copy.count(min_data)
#
#         # k가 현재 데이터 크기보다 작다면 답 출력
#         if k < food_len * min_data_count:
#
#             for i in range(len(food_times_copy)):
#
#                 # k의 값이 0이면 i값을 출력해준다.
#                 if k == 0:
#                     test = 1
#
#                 if food_times[i] > 0:
#                     if test == 1:
#                         answer = i + 1
#                         break
#                     k -= 1
#
#         # k가 현재 데이터 크기보다 크다면
#         else:
#             k -= food_len * min_data_count
#
#             # 최솟값까지는 이미 다 돈 것이므로 해당 값까지 빼기
#             food_times = [x - min_data_count for x in food_times]
#
#             # 0의 갯수는 지금 min_data가 있는 만큼은 빠졌으므로 해당 값을 빼준다.
#             food_len -= min_data_count
#
#         if answer != 0:
#             break
#
#         min_index += 1
#
#     return answer


import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0  # 직전에 다 먹은 음식시간
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]