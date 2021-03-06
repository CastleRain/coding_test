from collections import defaultdict

"""
단어 공부

문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""

"""
1. 리스트안에 저장한 후 cnt를 늘려간다
2. max를 이용해서 가장 큰 수를 찾는다
3. 같은 숫자가 있는지 파악한다
4. ord를 이용해서 대문자로 간다

a = 97 A = 65
max_len = ord('z') - ord('A') + 1
data = [0] * max_len

-> collections 이용해보는 첫 시간을 가져보자.

"""

dic = defaultdict(int)
count = 0


word = input().upper()

for w in word:
    dic[w] += 1

sort_dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)

# 정의된게 2개이상일 때 비교를 통해 ? 를할지 정답을 알려줄지 알려준다.

if len(sort_dic) >= 2:
    if sort_dic[0][1] == sort_dic[1][1]:
        print("?")
    else:
        print(sort_dic[0][0])
else:
    print(sort_dic[0][0])







