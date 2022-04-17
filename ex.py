# set = set()
# bankName = input('은행명 입력: ')
# set.add(bankName)
# print(set)

# dict = {}
# bankName = input('은행명 입력: ')
# id = input('id 입력: ')
# dict[bankName] = id
# print(dict)

# lotto = [1,2,3,4,5,6]
# print(len(lotto) < 6)


def hanoi(n, s=1, e=3):
    if n:
        hanoi(n - 1, s, 6 - s - e)
        print(s, e)
        hanoi(n - 1, 6 - s - e, e)


n = int(input())
cnt = (2 ** n) - 1
print(cnt)
if n < 21:
    hanoi(n)