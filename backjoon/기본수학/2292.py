"""
벌집


"""


"""

1 -> 7 -> 19 -> 37 -> 61 -> 91

an+1 = an + 6n + 1
이라는 점화식이 성립이된다.
이걸 다 구하고 비교하면 너무 시간 복잡도가 많을것같아서 이것을 쉽게 구하는 방법을 생각해내야한다.


3n^2-3n+1 n의 값보다 작은갯수만큼 이동가능
"""


n = int(input())

count = 1
cal = 0
while True:
    cal = (3*count**2) - (3*count) + 1

    if n <= cal:
        print(count)
        break
    count+=1