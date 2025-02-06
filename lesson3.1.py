
while True:
    login = input('Login: ')
    password = input('Password: ')
    if login == 'admin' and password == 'admin':
        print('Вы вошли как админ')
    else:
        print('Вы вошли как пользователь')
        break