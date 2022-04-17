class Parent:
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('이 객체의 이름은 %s 이고 나이는 %d 입니다.' % (self.name, self.age))


parent = Parent('방기진', 41)
parent.display()


class Child(Parent):
    spices = None

    def __init__(self, name, age, spices):
        super().__init__(name, age)
        self.spices = spices

    def display(self):
        print('이 객체의 이름은 %s 이고 나이는 %d 이며, 종은 %s 입니다.' % (self.name, self.age, self.spices))


child = Child('May', 14, 'puppy')

child.display()
