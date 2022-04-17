'''
Q.  다음 height 변수에 별(asterisk)의 층수를 입력하면 각 층 마다 별의 개수가 한 개씩 증가하여 출력되고, 마지막 줄에 별의 총 개수를 출력되도록 하는 코드를 작성하시오.
'''


def asterisk(bal):
    sum = 0
    for i in range(1, bal + 1):
        print("*" * i)
        sum += i
    return sum


bal = int(input("층 수 입력:"))
# print("총 별의 개수:", asterisk(bal))
print("총 별의 개수: %d"%asterisk(bal))

'''
FEEDBACK
    1) 출력방식을 '%d'로 바꿔보자
'''
