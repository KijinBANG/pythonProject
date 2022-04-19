'''
다음 emp 변수는 '입사년도-이름-급여'순으로 사원의 정보가 기록된 자료이다.
emp 변수를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.

입력예제:
    emp = ['2014홍길동220', '2002이순신300', '2010유관순260']

출력예제:
    names = ['홍길동', '이순신', '유관순']
'''

from re import findall


def nameExtractor(list) -> list:
    result = []
    for temp in list:
        result.append(findall('[가-힣]+', temp))
    return result


emp = ['2014홍길동220', '2002이순신300', '2010유관순260']
print(nameExtractor(emp))