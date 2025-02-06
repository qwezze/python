#ООП
'''
Создание класса для управления банковским счетом
Задача: Создать класс BankAccount, который будет представлять банковский счет. Он должен поддерживать следующие операции:
•	Внести деньги на счет.
•	Снять деньги со счета.
•	Проверить баланс.
•	В случае недостатка средств при снятии, выводить сообщение об ошибке
'''

class BankAccount:
    def __init__(self,user, balance=0):
        self.user=user
        self.balance=balance
    def deposit(self,balance):
        self.balance += balance
        print("Внесено", balance,"Текущий баланс", self.balance)

    def snimat(self,balance):
        if balance > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= balance
            print("Снято", balance, "Текущий баланс", self.balance)
    def get_balance(self):
        print("Текущий баланс", self.balance)


user1=BankAccount("Андрей", 10000)
user1.deposit(5000)
user1.get_balance()
user1.snimat(10000)
user1.get_balance()