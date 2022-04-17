'''
IP 별로 트래픽의 합계를 구하시오.
'''

traffic = {}

with open('./log.txt', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        if not log[-1].isdigit():
            log[-1] = '0'
        traffic[log[0]] = traffic.get(log[0], 0) + int(log[-1])

ret = sorted(traffic.items(), key=lambda x:x[1], reverse=True)

# for key in traffic:
#     val = traffic[key] // 1024
#     print("IP:", key, "인 traffic 총 량은", format(val, ',d'), "KB 입니다.")

print('[사용자IP] - [서비스용량]')
for ip, b in ret:
    KB = format(b // 1024, ',d')
    print('[%s] - [%s]'%(ip, KB), 'KB')