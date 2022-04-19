'''
다음 emp 변수는 '입사년도-이름-급여'순으로 사원의 정보가 기록된 자료이다.
emp 변수를 이용하여 아래와 같이 출력하는 함수를 정의하시오.

입력예제:
    emp = ['2014홍길동220', '2002이순신300', '2010유관순260']

출력예제:
    전체 급여 평균: 260
    평균 이상 급여 수령자
        이순신 => 300
        유관순 => 260
'''

from re import findall
from statistics import mean


def getInfo(list) -> None:
    names, pays = [], []
    for temp in list:
        names.append(''.join(findall('[가-힣]+', temp)))
        # print(names[-1])
        # print(type(names[-1]))
        # print(temp.split(names[-1]))
        pays.append(int(temp.split(names[-1])[-1]))
    avg = mean(pays)
    print('전체 급여 평균:', avg)
    for name, pay in zip(names, pays):
        if pay >= avg:
            print('\t{} => {}'.format(name, pay))


emp = ['2014홍길동220', '2002이순신300', '2010유관순260']
getInfo(emp)