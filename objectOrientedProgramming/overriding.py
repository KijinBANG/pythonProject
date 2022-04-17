class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass


class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus):
        pay = base + bonus
        print('총 수령액: ', format(pay, ',d'), '원')


class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        pay = tpay * time
        print('총 수령액: ', format(pay, ',d'), '원')


while True:
    print('직원의 급여 계산을 시작합니다.')
    print('1. 정규직 직원의 급여 계산')
    print('2. 임시직 직원의 급여 계산')
    print('3. 작업 종료')
    pOrT = input('원하는 작업 선택: ')
    try:
        pOrT = int(pOrT)
    except:
        print('올바른 값을 입력하세요.')
        continue
    if pOrT == 1:
        name = input('직원 이름 입력: ')
        base, bonus = map(int, input('직원의 \'급여\'와 \'보너스\'를 공백으로 구분하여 입력: ').split())
        emp = Permanent(name)
        emp.pay_calc(base, bonus)
    elif pOrT == 2:
        name = input('직원 이름 입력: ')
        tpay, time = map(int, input('직원의 \'시급\'과 \'총 근무시간\'을 공백으로 구분하여 입력: ').split())
        emp = Temporary(name)
        emp.pay_calc(tpay, time)
    elif pOrT == 3:
        break
    else:
        print('해당하는 서비스가 없습니다.')