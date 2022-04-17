'''
write code that sum up from 1 to input data = n
'''

num = int(input('언제 까지 더할지 입력: '))


def sumUp(n):
    if n == 1:
        return 1
    else:
        return n + sumUp(n - 1)


print(sumUp(num))