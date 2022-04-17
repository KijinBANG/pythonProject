'''
주어진 list 안에 저장된 단어의 개수를 dict에 저장하는 코드를 작성하시오.
'''

words = ['python', 'java', 'python', 'R', 'python', 'python', 'sql', 'javascript', 'javascript', 'c++', 'c++', 'c++']
dict = {}
for word in words:
    dict[word] = dict.get(word, 0) + 1

for key in dict:
    print(key, '이/가 ', dict[key], '번 등장합니다.', sep='')