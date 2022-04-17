'''
write code that return the value of n!
'''

num = int(input('Enter Number: '))


def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(num))