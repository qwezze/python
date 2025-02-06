print('hello world')
a = int(input('a=')) #'11' -> 11
b = float(input('b=')) #'10' -> 10.0
'''
+
-
*
/
% остаток от деления (11 % 2 = 1)
// целая часть от деления (11 // 2 = 5)
** степень чсила (10 ** 3 = 1000) 


and, or, not

==
>
<
>=
<=
!=
'''
print(10 == 10 and 11 == 11) #True and True -> True
print(10 > 8 and 10 < 12 and 10 == 10) #True

print(10 > 8 or 5 != 5) #True or False -> True
print(10 > 6 and (7 == 7 or 4 != 3)) #True

print(not 10 == 10) #False

c = 1
c += 1
c -= 1
c *= 1
c /= 1
c %= 1 #c = c % 1
c //= 2 #c = c // 2



a = 10
b = 20
if a > b:
    print(a + b)
elif a == b:
    print(a % b)
elif a < b:
    print(a // b)


if a % 5 == 0 and not a % 7 == 0:
    print(a)

