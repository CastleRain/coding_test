def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count
        
    answer = sorted(answer, key = lambda t:t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

# import heapq

# def solution(N, stages):
#     # 전체 스테이지 개수 : N
#     """
#     stage 정렬
#     1 2 2 2 3 3 4 6
#     1 -> 1을 가지고있는사람 / 자기보다 큰사람 (실패율, stage)
#     2 -> 2를 가지고있는사람 / 자기보다 큰사람

#     실패율 기준 정렬 => 실패율에 -를 붙여서 역순으로 정렬한다.
#     이후 pop을 하며 stage를 가져오자
#     """
#     answer = []
#     q = []
#     max_data = max(stages)

#     N_count = len(stages)
#     for i in range(1, N+1):
#         c = stages.count(i)
#         fail_ratio  = (c / N_count )
#         N_count = N_count-c
#         heapq.heappush(q, (-fail_ratio, i))
#     while q:
#         answer.append(heapq.heappop(q)[1])



#     return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]

    
    # [3,4,2,1,5]
    
    print(solution(N, stages))