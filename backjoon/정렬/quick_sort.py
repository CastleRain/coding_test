"""
퀵 소트

1. 처음을 피벗으로 설정하고 자신 다음 숫자(왼쪽에서부터) 하나씩 증가하면서 자신보다 높은 숫자를 선택한다.
2. 오른쪽부터 진행하여 피벗보다 작은수를 선택한다.
3. 선택된 두 숫자의 위치를 변환한다.
4. 왼쪽과 오른쪽이 교차 하는 위치에 피벗을 가져다 놓고 왼쪽과 오른쪽을 다시 퀵 소트를 진행한다.


"""

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # 4. 교차하기 직전까지 반복문 진행
    while left <= right:

        # 피벗보다 큰 데이터를 찾을때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1

        while right > start and array[right] >= array[pivot]:
            right -=1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[pivot] = array[pivot], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


