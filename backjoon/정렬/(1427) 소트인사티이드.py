"""
문제 링크 : 1427
푼 날짜 : 220314
문제 유형 : 정렬


풀이 : 


"""


if __name__ == "__main__":
    data = sorted(list(map(int, input())), reverse=True)
    print("".join(map(str, data)))
