'''
직사각형의 가로의 길이와 세로의 길이를 입력받아서,
넓이와 둘레를 제공하는 클래스를 만들어보자!
'''


class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        return area

    def peri_calc(self):
        perimeter = 2 * (self.height + self.width)
        return perimeter


width, height = map(int, input('직사각형의 가로의 길이와 세로의 길이를 공백으로 구분하여 입력: ').split())
rec = Rectangle(width, height)
print('직사각형의 넓이: ', rec.area_calc())
print('직사각형의 둘레: ', rec.peri_calc())
