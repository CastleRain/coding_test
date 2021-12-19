"""
후위 표기식
https://www.acmicpc.net/problem/1918

첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다.

그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다.

표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다.
"""


"""
풀이:

우선순위가 중요하다.

( ) <  + -   <  *  /
 0      1         2  

)가 나온경우 (이 나올때까지 pop을 진행한다.


"""

data = input()

# postfix = 후위 표기법이 저장되는 위치
postfix = []

# oper_st : 연산자 저장되는 위치
oper_st = []

# oper : 연산자 우선순위 저장되는 위치
oper = {
    "(" : 99,
    ")" : 0,
    "-" : 1,
    "+" : 1,
    "/" : 2,
    "*" : 2
}

for d in data:

    # 연산자라면
    if d in oper:

        # )이 온경우
        if d == ")":

            # ( 나오면 while문 종료
            while True:
                find_oper = oper_st.pop()
                if find_oper == "(":
                    break
                postfix.append(find_oper)

        else:
            # oper_st안에 아직 데이터가 없는경우 바로 저장
            if len(oper_st) == 0:
                oper_st.append(d)
            # 아닌경우 마지막 데이터와 우선순위 비교
            # 마지막 데이터보다 우선순위가 낮거나 같으면 pop하여 postfix에 저장
            else:

                while oper[d] <= oper[oper_st[-1]]:

                    # (인경우는 제외시켜야함
                    if oper_st[-1] =="(":
                        break

                    postfix.append(oper_st.pop())
                    if len(oper_st) == 0:
                        break
                oper_st.append(d)
    # 연산자가 아니라면 postfix에 저장
    else:
        postfix.append(d)

# 남은 oper_st pop하여 저장
for i in range(len(oper_st)):
    postfix.append(oper_st.pop())

print("".join(postfix))



# 뭔가 어설프게 코딩이 되었는데 진행이 되었다. 실제 정답을 보러가보자.
