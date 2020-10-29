import re

x = 1 + 2
b = type(x)

a = re.search('int|str|tuple|list|set',str(b))
print('Эта функция выводит тип объекта')


sqs = 0,1,4,9,16,25,36,49,64,81
print(sqs[7:5:-1])



class Person():

    def __init__(self, name, age, male):
        self.name = name
        self.age = age
        self.male = male

    def myInfo(self):
        print('My name is ' + self.name + ', and I\'m ' + str(self.age) + ' year, ' + self.male)


q = Person('Islam', 18, 'Famale')
print(q.name)

class Child(Person):

    def __init__(self, name, age, male, weight):
        super().__init__(name, age, male)
        self.weight = weight

    def getChildWeight(self):
        print('Я вешу ' + str(self.weight) + ' кг')


child = Child('Max', 1, 'Baby', 6)
child.myInfo()
child.getChildWeight()
