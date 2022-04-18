'''
write code that explains how the disks moves.
'''

num = int(input('Enter the number of disks: '))

# def move(n, start, to):
#     print("{}번 원반을 {}에서 {}로 옮긴다.".format(n, start, to))
#
#
# def hanoi(n, start, to, via):
#     if n == 1:
#         move(1, start, to)
#     else:
#         hanoi(n - 1, start, via, to)
#         move(n, start, to)
#         hanoi(n - 1, via, to, start)


# def hanoi(num, start=1, end=3):
#     if num:
#         hanoi(num-1, start, 6-start-end)
#         print(num, '번 원판을 ', start, '에서', end, '로 옮깁니다.')
#         hanoi(num-1, 6-start-end, end)


poles = ['A', 'B', 'C']


def hanoi(n, start=0, end=2):
    if n:
        hanoi(n - 1, start, 3 - start - end)
        print('{}번 원판을 {}에서 {}로 옮깁니다.'.format(n, poles[start], poles[end]))
        hanoi(n - 1, 3 - start - end, end)


hanoi(num)
