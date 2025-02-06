#функции

#min(1,2,4) #1
#max(4,5,6) #6


def summa(a,b,c): #определение ф-ции a,b,c - параметры ф-ции (входные данные)
    #a=3 b=4 c=5
    print(a + b + c)

summa(10, 20, 30)
summa(3, 4, 5)

'''
return точка выхода из ф-ции, то что ф-ция возвращает 
'''
def min_numbers(a,b,c):
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < a and c < b:
        return c


c = min_numbers(2, 4, 10) #c=1
print(c)

print(c ** 4)

def max_numbers(a=0,b=0,c=0):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
    return 0

print(max_numbers())
print(max_numbers(3))
print(max_numbers(4,5))



#lambda анонимная ф-ция

d = lambda a,b,c: a + b + c
print(d(4,5,6))



def filter(s, f):
    #f=lambda a: a % 2 == 0
    b = []
    for i in s:
        if f(i):
            b.append(i)
    return b

a = [1,2,3,4,5,6,7,8,9,10,12]
'''
12 % 10 -> 2
22 % 10 -> 2
'''
f = lambda a: a % 2 == 0 and a % 10 == 2
#f(6) -> True
#f(5) -> False


print(filter(a, f))




users = ['user1', 'user2', 'u3', 'u4', 'user5']
f = lambda login: len(login) > 4
def r_users(users, f):
    users_new = []
    for i in users:
        if f(i):
            users_new.append(i)
    return users_new
print(r_users(users, f))
#len('1234') #4

#декораторы
def select(input_func):
    def output_func():
        print('******************')
        input_func()
        print('******************')
    return output_func


@select
def hello():
    print('Hello world!')

hello()

@select
def summa():
    print(10 + 20 + 30)

summa()

