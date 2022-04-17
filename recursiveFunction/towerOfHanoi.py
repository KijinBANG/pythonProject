'''
write code that explains how the disks moves.
'''

num = int(input('Enter the number of disks: '))


def move(n, start, to):
    print("{}번 원반을 {}에서 {}로 옮긴다.".format(n, start, to))


def hanoi(n, start, to, via):
    if n == 1:
        move(1, start, to)
    else:
        hanoi(n - 1, start, via, to)
        move(n, start, to)
        hanoi(n - 1, via, to, start)


hanoi(num, 'A', 'C', 'B')
