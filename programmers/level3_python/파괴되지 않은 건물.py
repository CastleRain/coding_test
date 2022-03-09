"""
https://programmers.co.kr/learn/courses/30/lessons/92344

적의 공격을 얼마나 잘 막느냐가 관건이다.


skill = 1 : 적의 공격
skill = 2 : 우리팀 힐러
[type, r1, c1, r2, c2, degree]

( r1,c1)  ~ (r2, c2)

효율성을 높일려면 바로 한번에 계산이 진행되면 좋을 것 같다.
skill별로 계속 돌면서 하는것보단 한번돌때 한번에 계산하는것?

정렬을 r1 -> c1순서로 해놓자. 그러면 처음 돌때 그다음 행으로 갈때마다 제대로 애가 가져와진다.


1. 적의 공격이 없다면 그냥 통과
2. 적의 공격만 다 더해놓고 장벽이랑 비교해봤을 때 작다면 통과
3. 적의 공격이 방벽보다 높은 곳이 있다면 해당 지역만 힐 진행 => 최약의 경우 다 계산이 들어갈 것
"""

def solution(board, skill):
    answer = 0
    attack_num = 0
    who_attack_skill = sorted(skill, key = lambda x:x[0])
    
    # 공격한곳이 없다면 그냥 board만큼이 답이다.
    if who_attack_skill[0][0] == 2:
        answer = len(board) * len(board[0])

    for i in range(len(who_attack_skill)):
        while who_attack_skill[i][0] == 1:

    



    return answer



board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

skill_sort = sorted(skill, key = lambda x : (x[1], x[2]))
print(skill_sort)


print(solution(board, skill))