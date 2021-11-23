"""
잃어버린 괄호
https://www.acmicpc.net/problem/1541


세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

55-50+40
-> -35
"""

"""
내 풀이

후위표기법으로 진행해본다.
하다보니 후위표기법이 더 쉬운것같아 후위표기법 만들고 다시돌아온다.
연산이 + -만있으므로 괄호의 의미가 필요없이 전부 뒤로 보내면된다.

 
"""

data = input()

oper = ["+", "-"]

num = []
number = []
op = []
for i in data:

    if i in oper:
       op.append(i)
       # 현재까지 만들어진 number를 int로 변환하여 number에 저장
       number.append(int("".join(num)))
       num = []
    # 숫자인경우 nubmer에 추가.
    else:
        num.append(i)

# 마지막 숫자값 저장
number.append(int("".join(num)))

print(number)
# for _ in range(len(op)):
#     number.append(op.pop())
#
# print(number)
