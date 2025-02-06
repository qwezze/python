import random


#ООП (обьектно-ориентированое программирование)
'''
класс (представляет некоторую сущность)
объект (конкретное воплощение класса)
'''



class Person: #сущность (шаблон)
    def __init__(self, name, age): #конструктор
        self.name = name
        self.age = age

    #атрибуты и методы


    #методы
    def info(self):
        print(f'Name: {self.name} Age: {self.age}')

vasia = Person('Вася', 22) #создание объекта
alex = Person('Александр', 18) #создание объекта
user1 = Person('User1', 18)
user2 = Person('User2', 18)

print(vasia.name)
print(alex.name)

vasia.info()
user1.info()



#принципы ООП

#наследование


class Person:# базовый (суперкласс)
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f'Name: {self.name}')

    def display_all_info(self):
        print(f'Name: {self.name} Company: {self.company} Salary: {self.salary}')



class Employee(Person): #дочерний
    def __init__(self, company, salary, name):
        self.company = company
        self.salary = salary
        super().__init__(name)


    def work(self):
        print(f'{self.name} аботает')

    def display_info(self):
        print(f' {self.name}')


#создать 100 обьектов случайно сгенироваными данными


users = []
for i in range(0, 100):
    users.append(Employee('Yandex', random.randint(1000, 10000), f'User{i+1}'))

for user in users:
    user.display_all_info()


#инкапсуляция (скрытие данныъх)
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._password = 'asfaf'
a = A(10, 20)
print(a)



