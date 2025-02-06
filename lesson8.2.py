'''
Создать класс для управления задачами
'''
class Task:
    def __init__(self, title, description, status=False):
        self.title = title
        self.description = description
        self.status = status
        self.completed = True
        self.filename = 'tasks.txt'


    def completed(self):
        self.completed = False


    def status_change(self):
        self.status = True


    def to_save_txt(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(f'{self.title},{self.description},{self.status}')
            f.close()

task1 = Task('Изучить Python', 'Пройти уроки по Python')
task1.status_change()
task1.to_save_txt()



