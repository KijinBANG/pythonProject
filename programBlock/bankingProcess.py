'''
Q.  중첩함수를 적용하여 다음 <조건>에 맞게 은행 계좌 함수의 빈 칸을 채우시오.
    <조건1>   외부함수:   bank_account(): 잔액(balance) outer변수
'''

def bank_account(bal):
    balance = bal

    def getBalance():
        print("현재 계좌의 잔액은", balance, "원 입니다.")

    def deposit(money):
        nonlocal balance
        if money > 0:
            balance += money
            print(money, "원 입금 후 잔액은", balance, "원 입니다.")
        else:
            print("적절한 금액이 아닙니다.")

    def withdraw(money):
        nonlocal balance
        if money > balance:
            print("잔액이 부족합니다.")
        else:
            balance -= money
            print(money, "원 출금 후 잔액은", balance, "원 입니다.")

    return getBalance, deposit, withdraw  # 클로저 함수 리턴

bal = int(input("최초 계좌의 잔액 입력:"))
getBalance, deposit, withdraw = bank_account(bal)

while True:
    print("1. 잔액 확인")
    print("2. 입금")
    print("3. 출금")
    print("4. 종료")
    selection = int(input("원하는 작업 선택:"))
    if selection == 1:
        getBalance()
    elif selection == 2:
        money = int(input("입금액 입력:"))
        deposit(money)
    elif selection == 3:
        money = int(input("출금액 입력:"))
        withdraw(money)
    elif selection == 4:
        break
    else:
        print("적절한 입력값이 아닙니다.")

'''
FEEDBACK
    1) 'switch' 함수와 같은 형태로 코드를 작성 해 보자.
'''