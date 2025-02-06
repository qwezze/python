'''
Задача: Создать класс User, который будет представлять пользователя. От него унаследовать классы Admin и Guest, которые будут иметь разные уровни доступа.
'''
class User:
    def __init__(self,login,password):
        self.login = login
        self.password = password
    def level(self):
        return "обычный пользователь"

class Admin(User):
    def level(self):
        return "администратор"
class Guest(User):
    def level(self):
        return "гость"

a = Admin("user1", "12345")
print(a.level())
b = Guest("user2", "56789")
print(b.level())
c = User("user3", "15766")
print(c.level())