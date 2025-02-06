#работа с файлами и папками (каталоги)

'''
read (r)
write (w)
append (a)
'''


#f = open('1.txt', 'r')
#print(f.read())
#print(f.read(20))
#print(f.readlines())
#print(f.readline())

'''f = open('numbers.txt', 'r')
d = f.read()
f.close()
a = d.split(' ')

a = list(map(int, a))
print(a)

b = []
for i in  a:
    b.append(int(i))
print(b)'''



'''
'24 2 31 2 43 22 33 4' -> [24, 2, 31, 2, 43, 22, 33, 4]
'
f = open('users.txt', 'w')
f.write('user2')
f.close()

f = open('users.txt', 'a')
f.write('user3')
f.close()'''

#with as

#with open('users.txt') as f: #f = open('users.txt', 'a')
#    print(f.read())
#    f.close()

#with open('users.txt', 'w', encoding='utf-8') as f:
#    f.write('привет')
#    f.close()

#запросить у пользователя числа в диапазоне от 1 до 100 Каждое число записывать в конец файла numbers.txt. Оканчанием ввода данных является 0
'''
while True:
    n = int(input('Введите число в диапазоне от 1 до 100: '))
    if n == 0:
        break
    if n >= 1 and n < 101:
        with open('numbers.txt', 'a') as f:
            f.write(str(n) + '\n')
            f.close()
        print('Число записано')
    else:
        print('Ошибка ввода')


with open('number1.txt') as f1, open('number2.txt') as f2, open('result.txt', 'w') as res:
    a = int(f1.read())
    b = int(f2.read())
    res.write(str(a + b) + '\n')
    res.write(str(a - b) + '\n')
    res.write(str(a * b) + '\n')
    res.write(str(a / b) + '\n')
    res.write(str(a % b) + '\n')
    res.write(str(a // b) + '\n')
    f1.close()
    f2.close()


with open("numbers.txt") as f1:
    a = f1.readlines()
    s = 0
    for i in a:
         s += int(i.strip('\n'))
    f1.close()
print(s)'''

#Определить самую длинную строку в файле
'''
1. ПРочитать файл 
2. Циклом перебрать каждую строку
4. len()
5. max(), if
6. зАкрываете файл



with open('text.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n')
    print(len(max(data)))
    
    
a = [1,2,3,4,5]
print(len(a)) #5
b = 'hello'
print(len(b)) #5'''