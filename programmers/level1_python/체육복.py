def solution(n, lost, reserve):
    answer = 0
    
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    set_lost_copy = set_lost.copy()
    for los in set_lost_copy:
        if los-1 in set_reserve:
            set_lost.remove(los)
            set_reserve.remove(los-1)
        elif los+1 in set_reserve:
            set_lost.remove(los)
            set_reserve.remove(los+1)
            
    answer = n - len(set_lost)
    return answer

if __name__ == "__main__":
    
    n = 5
    lost = [2,4]
    reserve = [1,3,5]

    # 5

    
    print(solution(n, lost, reserve))
#     """
#     0. 옷 있는데 여분 없는사람 = 0
#     1. 옷 잃은사람 = 1
#     2. 옷 잃고 옆에 여분이 없는 경우 = 2 
#     3. 여분 있는 사람 = 3
#     4. 여분옷을 분배 순서 2 -> 1
#     """
#     data = [-1] * 32
    
#     for i in range(1,n+1):
#         data[n] = 0
    
#     for res in reserve:
#         data[int(res)] = 3
        
#     for los in lost:
#         if data[int(los)] == 3:
#             data[int(los)] = 0
#         else:
#             data[int(los)] = 1
            
#     for j in range(1, n+1):
#         data_now = data[j]
#         data_next = data[j+1]
        

#         if (data_next in [0,1,2]) and (data_now in [0,1,2]):
#             if data_now == 1:
#                 data[j] = 2
        

    
#     for k in range(1,n+1):
#         if data[k] == 3:
#             if (data[k-1] in [1,2]) or (data[k+1] in [1,2]):
#                 if data[k-1] == 2:
#                     data[k-1] = 0
#                     data[k] = 0
#                 elif data[k+1] == 2:
#                     data[k+1] = 0
#                     data[k] = 0
#                 elif data[k-1] == 1:
#                     data[k-1] = 0
#                     data[k] = 0
#                 elif data[k+1] == 1:
#                     data[k+1] = 0
#                     data[k] = 0
                    
#     for res in range(1,n+1):
#         if data[res] != 1:
#             answer+=1
