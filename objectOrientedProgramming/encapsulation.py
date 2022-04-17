class Account:
    # private member variable
    __balance = 0
    __accName = None
    __accNo = None

    # constructor : initialize member variables
    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    def deposite(self, money):
        if money > 0:
            self.__balance += money
            print('{}원을 입금하여, 현재 잔액은 {}원 입니다.'.format(money, self.__balance))
        else:
            print('금액을 확인 해 주세요.')
            return

    def withdraw(self, money):
        if money < self.__balance:
            self.__balance -= money
            print('{}원이 출금되어, 현재 잔액은 {}원 입니다.'.format(money, self.__balance))
        else:
            print('잔액이 부족합니다.')
            return

dict = {}

while True:
    print('1. 계좌등록')
    print('2. 계좌정보확인')
    print('3. 입금')
    print('4. 출금')
    print('5. 종료')
    decision = int(input('원하는 작업 선택: '))
    if decision == 1:
        bankName = input('은행명 입력: ')
        id = input('id 입력: ')
        if bankName in dict :
            print('계좌가 이미 존재합니다.')
        else:
            balance, name, no = input('최초 예치금, 계좌명, 계좌번호를 공백으로 구분하여 입력:').split()
            balance = int(balance)
            dict[bankName] = id
            dict[bankName] = Account(balance, name, no)
            print('계좌가 성공적으로 등록되었습니다.')
    elif decision == 2:
        bankName = input('은행명 입력: ')
        if bankName in dict:
            bal, name, no = dict[bankName].getBalance()
            print('계좌명: ', name)
            print('계좌번호: ', no)
            print('잔액: ', format(bal, ',d'), '원')
        else:
            print('해당 계좌가 존재하지 않습니다.')
    elif decision == 3:
        bankName = input('은행명 입력: ')
        if bankName in dict:
            money = int(input('입금 금액 입력: '))
            dict[bankName].deposite(money)
        else:
            print('해당 계좌가 존재하지 않습니다.')
    elif decision == 4:
        bankName = input('은행명 입력: ')
        if bankName in dict:
            money = int(input('출금 금액 입력: '))
            dict[bankName].withdraw(money)
        else:
            print('해당 계좌가 존재하지 않습니다.')
    elif decision == 5:
        break
    else:
        print('올바른 값이 아닙니다.')

'''
function is the first class object in PYTHON
try to eliminate duplicate code.
'''