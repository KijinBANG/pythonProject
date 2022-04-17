c = int(input())
li = list(map(int, input().split()))
min = 100
max = 0
sum = 0
for i in li:
    min = min if min < i else i
    max = max if max > i else i
    sum += i
sum -= (min + max)
print(sum)