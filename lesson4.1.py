#while, for
'''
i = 0
while i < 10:
    print(i)
    i += 1

while True:
    print(1)'''

users = []
#users = ['user1','user2','user3']

while True:
    print('1 - регистрация\n2 - авторизация\n3 - выход')
    n = int(input('Ваш выбор:'))
    if n == 1:
        login = input('Логин: ')
        if login in users:
            print('Такой логин уже существует')
        else:
            users.append(login)
            print('Вы успешно прошли регистрацию!')
    elif n == 2:
        login = input('Логин: ')
        if login in users:
            print('Вы успешно прошли авторизацию')
    elif n == 3:
        break
