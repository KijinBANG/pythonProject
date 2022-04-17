class Flight:
    def fly(self):
        print('날다!, fly 함수의 원형')


class Plane(Flight):
    def fly(self):
        print('비행기가 날다!')


class Kite(Flight):
    def fly(self):
        print('연이 날다!')


class Insect(Flight):
    def fly(self):
        print('곤충이 날다!')


class Bird(Flight):
    def fly(self):
        print('새가 날다!')

while True:
    print('\n원하는 작업 선택: ')
    print('1. 날기만 하면 O.K.')
    print('2. 비행기')
    print('3. 연')
    print('4. 곤충')
    print('5. 새')
    print('6. 종료')
    choice = input('원하는 작업을 선택: ')
    try:
        choice = int(choice)
    except:
        print('숫자만 입력하세요.')
        continue
    flight = Flight()
    if choice == 1:
        flight = Flight()
    elif choice == 2:
        flight = Plane()
    elif choice == 3:
        flight = Kite()
    elif choice == 4:
        flight = Insect()
    elif choice == 5:
        flight = Bird()
    elif choice == 6:
        break
    else:
        print('해당하는 서비스가 없습니다.')
        continue
    flight.fly()
