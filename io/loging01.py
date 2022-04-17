'''
log.txt 파일을 읽어서 행의 개수를 출력하시오.
'''

pageviews = 0

with open('./log.txt', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        # print(type(log))
        # print(log, '\nlen(log):', len(log))
        status = log[8]
        # print('type(status):', type(status))
        # print('status:', status)
        if status == '200':
            pageviews += 1

print(pageviews)