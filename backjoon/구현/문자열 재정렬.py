"""
이코테 p322

문자열 재정렬

알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어진다.

이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

K1KA5CB7 -> ABCKK13

AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20

쉽게 숫자를 제외한 문자열을 만든 후 sort를 진행하고 뒤에 숫자를 이어붙이자.

"""
# 내 풀이
# n = input()
#
# number = 0
# letter = []
#
# for data in n:
#     if data in ['0','1','2','3','4','5','6','7','8','9']:
#         number += int(data)
#
#     else:
#         letter.append(data)
#
# letter.sort()
# letter.append(str(number))
# print("".join(letter))

# 책풀이

n = input()

number = 0
letter = []

for data in n:
    if data.isalpha():
        letter.append(data)


    else:
        number += int(data)

letter.sort()

if number != 0:
    letter.append(str(number))
print("".join(letter))
