"""

https://www.acmicpc.net/problem/18406

"""

score = int(input())

score_len = len(str(score))

left_score = 0
right_score = 0

for i in range(score_len):
    if i < score_len / 2:
        right_score += score % 10
        score = int(score / 10)
    else:
        left_score += score % 10
        score = int(score / 10)

if right_score == left_score:
    print("LUCKY")
else:
    print("READY")
