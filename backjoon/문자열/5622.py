"""
다이얼
https://www.acmicpc.net/problem/5622


"""

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS" ,  "TUV", "WXYZ"]

word = input()
result = 0
# 단어 하나씩 불러오기
for w in word:

    # 다이얼 리스트 인덱스 하나씩 불러오기
    for i in range(len(dial)):

        # 만약 현재 다이얼 인덱스안에 해당 단어가 있다면
        if w in dial[i]:

          # A부터 3초가 걸리므로 +3을 한다.
          result += i+3

print(result)