
age = 20
if age > 18:
    print('Доступ разрешен')



'''
>
<
>=
<=
!=
'''
x = 10
y = 20
print(x > y) #False
print(x < y) #True
print(x >= y) #False
print(x <= y) #True


#if x > y:
#    print('x > y')
age = 19
if age == 18:
    print('age 18')
elif age == 19: #True
    print('age 19')
elif age == 19:
    print('age 19')

'''
Булевая логика
Логическое умножение (and)
False(0) and False(0) -> False(0)
False(0) and True(1) -> False(0)
True(1) and False(0) -> False
True(1) and True(1) -> True 
'''
age = 20
if age >= 18 and age <= 40: #True and True -> True
    print('Ok')

'''
Логическое сложение (or)
False(0) or False(0) -> False(0)
False(0) or True(1) -> True(1)
True(1) or False(0) -> True(1)
True(1) or True(1) -> True(1)
'''
x = 10
y = 20
if x > y or x == y: #False or False -> False
    print('Ok')

'''
Отрицание not
not False -> True
not True -> False 
'''
x = 10
y = 20
if not x > y: #not False -> True
    print('Ok')


