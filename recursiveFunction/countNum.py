'''
print numbers from 1 to input data = n
'''

num = int(input('마지막 숫자 입력: '))


def recursiveFunction(n):
    if n > 0:
        recursiveFunction(n - 1)
    else:
        return
    print(n)


recursiveFunction(num)
