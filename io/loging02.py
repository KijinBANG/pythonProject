'''
로그 파일을 읽어서 접속한 컴퓨터의 대수를 구하시오.
    - 각 행의 첫번째 데이터는 접속한 컴퓨터의 IP 입니다.
    - 이 데이터의 중복을 제거한 데이터의 개수가 컴퓨터의 개수 입니다.
'''

set = set()

with open('./log.txt', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        set.add(log[0])

print(len(set))