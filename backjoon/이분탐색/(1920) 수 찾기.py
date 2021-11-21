"""
수 찾기
N <200,000

"""


input()
first_data = list(map(int, input().split()))
input()
second_data = list(map(int, input().split()))

first_data.sort()


def binary_search(array, target, start, end):

    mid = (start + end) // 2
    if start > end:
        return None

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

for second in second_data:
    if binary_search(first_data, second, 0, len(first_data)-1) != None:
        print("1")
    else:
        print("0")