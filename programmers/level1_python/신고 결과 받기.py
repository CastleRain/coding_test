# created : 22.01.14
# by CastleRain




def solution(id_list, report, k):

    # 중복 항목 제거
    report = list(set(report))



    answer = []
    return answer


if __name__ == "__main__":

    id_list =["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    # [2,1,1,0]

    print(solution(id_list, report, k))