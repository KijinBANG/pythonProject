'''
about 'Quick Sort'
    - 찰스 앤터니 리처드 호어(Charles Antony Richard Hoare)가 개발한 정렬 알고리즘
    - 퀵 정렬은 불안정 정렬 에 속하며, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬 에 속한다.
    - 분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법
    - 합병 정렬(merge sort)과 달리 퀵 정렬은 리스트를 비균등하게 분할한다.
    - 분할 정복(divide and conquer) 방법
    - 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략이다.
    - 분할 정복 방법은 대개 순환 호출을 이용하여 구현한다.
'''

array = [15, 27, 93, 30, 32, 19, 26, 72, 14, 8]


def qSort(list):
    terminal = len(list) - 1

    def quick_sort(list, start=0, end=terminal):
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end

        while left <= right:
            while left <= end and list[left] <= list[pivot]:
                left += 1
            while right > start and list[right] >= list[pivot]:
                right -= 1
            if left > right:
                list[right], list[pivot] = list[pivot], list[right]
            else:
                list[left], list[right] = list[right], list[left]
        quick_sort(list, start, right - 1)
        quick_sort(list, right + 1, end)

    quick_sort(list)


print('before:', array)
qSort(array)
print('after:', array)
