"""
created 22.01.14
by CastleRain



"""
from collections import defaultdict
def solution(N, stages):

    cnt = len(stages)
    for i in range(1, len(stages)+1):
        
        data_cnt = stages.count(i)

        data[i] = data_cnt / cnt
        
        cnt -= data_cnt
    print(data)
    return 1

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]

    
    # [3,4,2,1,5]
    
    print(solution(N, stages))