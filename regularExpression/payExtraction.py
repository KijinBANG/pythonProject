'''
다음 emp 변수는 '입사년도-이름-급여'순으로 사원의 정보가 기록된 자료이다.
emp 변수를 이용하여 전체 사원의 급여의 평균을 리턴하는 함수를 정의하시오.

입력예제:
    emp = ['2014홍길동220', '2002이순신300', '2010유관순260']

출력예제:
    전체 사원 급여 평균 = 260
'''

from re import findall


def getAvg(list) -> int:
    sum = 0
    for info in list:
        sep = ''.join(findall('[가-힣]+', info))
        sum += int(info.split(sep)[1])
        print('sep:', sep, ', sum:', sum)
    return sum / len(list)


emp = ['2014홍길동220', '2002이순신300', '2010유관순260']
print(getAvg(emp))