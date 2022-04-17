'''
Q.  자연수 n 값을 입력받아서, n! 의 값을 출력하는 코드를 작성하시오. (재귀적 방법을 사용하시오.)
'''


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def nCk(n, k: int) -> int:
    return factorial(n)/(factorial(k)*factorial(n-k))


n = int(input('자연수 n의 값 입력: '))
print("n! 의 값: %d"%factorial(n))

n, k = map(int, input('n 과 k 의 값을 공백으로 구분하여 입력: ').split())
print("nCk 의 값: %d"%nCk(n, k))
'''
FEEDBACK
    1) 작성한 코드를 바탕으로 자연수 n,k 의 값을 입력받아, nCk 의 값을 구하는 코드도 짜 보도록 하자.
'''
