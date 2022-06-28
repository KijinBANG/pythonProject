import csv
import matplotlib.pyplot as plt

f = open('ta_20220628155123.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)

lst = []
tempDateLow, tempDateHigh, temp, m, M = "", "", 0.0, 0.0, 0.0
for row in data:
    for idx in range(2, 5):
        try:
            temp = float(row[idx])
        except:
            temp = 0.0
            lst.append(row)
        row[idx] = temp
    # print(row)
    # print("??", m, row[3], m > row[3])
    if m > row[3]:
        tempDateLow = row[0]
        m = row[3]
    if M < row[4]:
        tempDateHigh = row[0]
        M = row[4]
    # print("test", tempDateLow, m)
# print(lst)
print("가장 추웠던 날", tempDateLow, m)
print("가장 더웠던 날", tempDateHigh, M)
f.close()

plt.title("histogram")
plt.plot([12, 43, 25, 15], label='first')
plt.plot([10, 30, 20, 40], label='second')
plt.legend()
plt.show()
