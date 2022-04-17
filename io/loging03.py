'''
로그 파일을 읽어서 전체 트래픽을 구하시오.
    - 각 행의 마지막 데이터가 트래픽
    - 단위는 Byte 인데 KB 단위로 출력하시오. (1KB 는 1024 Byte)
'''

traffic = 0

with open('./log.txt', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        # try:
        #     traffic += int(log[-1])
        # except:
        #     traffic += 0
        if log[-1].isdigit():
            traffic += int(log[-1])

traffic = traffic // 1024
print(format(traffic, ',d'), 'KB')