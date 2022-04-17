'''
1~45 사이의 서로 다른 정수 6개를 입력받아서 list에 저장하는 코드를 작성하시오.

    - 정수 이외의 데이터가 들어오면 다시 입력받도록 작성하세요.
    - 1 ~ 45 사이의 숫자 이외의 데이터가 들어오면 다시 입력받도록 작성하세요.
    - 중복된 데이터가 들어오면 다시 입력받도록 작성하세요.
    - 숫자를 오름차순 정렬해서 출력하세요.
'''

lotto = []
idx = 1
while idx < 7:
    try:
        print(idx, end="")
        val = int(input('번째 번호 입력: '))
        if val < 1 or val > 45:
            print('1 ~ 45 사이의 값만 입력하세요.')
            continue
        if val in lotto:
            print('이미 입력한 번호입니다.')
            continue
        lotto.append(val)
        idx += 1
    except:
        print('숫자만 입력하세요.')

lotto.sort()
print(lotto)