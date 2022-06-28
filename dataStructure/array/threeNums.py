'''
3개의 수의 값이 0이 되는 데이터의 인덱스 조회
(배열의 데이터는 중복되지 않음)

입력: [-1, 0, 1, 2, -4]
출력: [[-1, 0, 1]]
'''

from itertools import combinations


def threeNums(li) -> list:
    result = []
    temp = list(combinations(li, 3))
    # print(temp)
    for tmp in temp:
        # print(tmp)
        # print(sum(tmp))
        if sum(tmp) == 0:
            result.append(tmp)
    return result


data1 = [-1, 0, 1, 2, -4]
data2 = [-1, 0, 1, 2, -1, -4]
print(threeNums(data2))