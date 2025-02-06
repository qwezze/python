'''
Задача
запросить у пользователя 3 значения и найти минимальный и максимальный из них и вывести
'''

x = int(input('x='))
y = int(input('y='))
z = int(input('z='))

if x < y and x < z:
    print('min=', x)
if y < x and y < z:
    print('min=',y)
if z < x and z < y:
    print('min=',z)


if x > y and x > z:
    print('max=',x)
if y > x and y > z:
    print('max=',y)
if z > x and z > y:
    print('max=',z)



