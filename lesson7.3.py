#обработка ошибок
a = 10
b = 20
print(a + b)

#print(10 / 0)
b = [1,2,3]
try:
    print(b[7])
except ZeroDivisionError:
    print('ошибка деления на 0')
print(1)