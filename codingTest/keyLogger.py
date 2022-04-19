'''
문제
    키로거는 사용자가 키보드를 누른 명령을 모두 기록한다.
    키로거가 설치된 컴퓨터에서 비밀번호를 입력할 때 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
    비밀번호 창에서 입력한 키가 주어졌을 때 비밀번호를 알아내는 프로그램을 작성하시오.
    키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.

입력
    첫째 줄에 테스트 케이스의 개수가 주어진다.
    각 테스트 케이스는 한줄로 이루어져 있고 입력한 순서대로 길이가 L인 문자열이 주어진다.(1 ≤ L ≤ 1,000,000)
    백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다.
    화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다.
    나머지 문자는 비밀번호의 일부이다.
    물론, 나중에 백스페이스를 통해서 지울 수는 있다.
    만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

출력
    각 테스트 케이스에 대해서, 강산이의 비밀번호를 출력한다. 비밀번호의 길이는 항상 0보다 크다.

예제 입력
    3
    <<BP>Cd-
    <BP<A>Cd-
    ThIsIsS3Cr3t

예제 출력
    BPC
    BAPC
    ThIsIsS3Cr3t
'''


class Solution:
    def keyLogger(self, data):
        stack_left = []
        stack_right = []
        for char in data:
            if char == '<':
                if stack_left:
                    stack_right.append(stack_left.pop())
            elif char == '>':
                if stack_right:
                    stack_left.append(stack_right.pop())
            elif char == '-':
                if stack_left:
                    stack_left.pop()
            else:
                stack_left.append(char)
        stack_left.extend(reversed(stack_right))
        return ''.join(stack_left)


n = int(input('몇 번 반복?: '))
solution = Solution()
for i in range(n):
    data = input('입력: ')
    print(solution.keyLogger(data))
