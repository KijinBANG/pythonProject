import random

angle = ['0', 'π/6', 'π/4', 'π/3',
         'π/2', '(2π)/3', '(3π)/4', '(5π)/6',
         'π', '(7π)/6', '(5π)/4', '(4π)/3',
         '(3π)/2', '(5π)/3', '(7π)/4', '(11π)/6']
fnc = ['sin', 'cos', 'tan']
f = random.choice(fnc)
q = random.choice(angle)

print('sec(π/6)의 값이 2/root(3) 이다.')
answer = input('{0}({1})의 값을 입력 : '.format(f, q))
print('정답인지아닌지 파악하는 로직은 아직 안말들었어요!')