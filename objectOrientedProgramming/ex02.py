'''
statistic 의 mean 과 math 의 sqrt 를 이용하여,
정수로 이루어진 어떤 dataset 이 주어졌을 때, 분산과 표준편차를 리턴하는 메소드를 포함한 클래스를 작성하시오.
'''

from statistics import mean
from math import sqrt


class Scattering:
    data = []

    def __init__(self, data):
        self.data = data

    def var(self):
        avg = mean(self.data)
        diff = [(val - avg) ** 2 for val in self.data]
        return sum(diff) / (len(self.data) - 1)

    def std(self):
        var = self.var()
        return sqrt(var)



data = [5, 9, 1, 7, 4, 6]
scattering = Scattering(data)
print('분산:', scattering.var())
print('표준편차:', scattering.std())
