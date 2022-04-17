'''
write code that return the value of n-th fibonacci sequence
'''

num = int(input('Enter number: '))


def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(num))