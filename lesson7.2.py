#замыкания


def outer(): #внешняя ф-ция
    n = 5

    def inner():
        nonlocal n
        n += 1
        print(n)
    return inner

f = outer()
f() #6
f() #7
f() #8

#область видимости переменных
a = 10
def b():
    #a = 12
    h = 11
    global a
    print(a)

b()

