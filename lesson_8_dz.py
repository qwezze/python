'''
Создайте класс `Employee` (Сотрудник), который имеет атрибуты:
- имя
- фамилия
- зарплата

Добавьте метод для расчета годовой зарплаты. Создайте подкласс `Manager` (Менеджер), который наследует от `Employee` и
добавляет дополнительный атрибут — бонус к зарплате. Перепишите метод расчета годовой зарплаты с учетом бонуса.
'''

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Зарплата: {self.salary}"


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, bonus):
        super().__init__(first_name, last_name, salary)
        self.bonus = bonus

    def annual_salary(self):
        return super().annual_salary() + self.bonus

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Зарплата: {self.salary}, Бонус: {self.bonus}"



employee = Employee("Иван", "Иванов", 50000)
manager = Manager("Петр", "Петров", 70000, 120000)

print(employee)
print("Годовая зарплата:", employee.annual_salary())
print(manager)
print("Годовая зарплата:", manager.annual_salary())