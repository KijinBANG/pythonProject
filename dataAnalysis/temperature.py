import csv

f = open('ta_20220628155123.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)

lst = []
tempDate, temp, m = "", 0.0, 0.0
for row in data:
    for idx in range(2, 5):
        try:
            temp = float(row[idx])
        except:
            temp = 0.0
            lst.append(row)
        row[idx] = temp
    # print(row)
    print("??", m, row[3], m > row[3])
    if m > row[3]:
        tempDate = row[0]
        m = row[3]
    print("test", tempDate, m)
# print(lst)
print(tempDate, m)
f.close()
