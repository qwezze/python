'''
Создайте класс Book с атрибутами:

title (название книги),
author (автор),
year (год издания).
Добавьте методы:

get_info(), который возвращает строку с информацией о книге в формате "Название: <title>, Автор: <author>, Год: <year>"
'''

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"
a = Book("Муму", "Тургенев","1854")
print(a.get_info())
b = Book ("Книга2", "Автор2", "1972")
print(b.get_info())

'''
tkinter
'''