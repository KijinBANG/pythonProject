'''
write code which build n-th-story isosceles triangle with '*'
'''
story = int(input('층수 입력: '))
for i in range(story):
    print(" "*(story - 1 - i), "*"*(i*2+1), sep="")