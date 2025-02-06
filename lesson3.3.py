#list (список)
a = 10 #integer
b = 10.5 #float
c = 'text' #string
d = False #boolean

l = [1,2,3,4,5,10, 'test', 11.1]
#    0 1 2 3 4 5     6      7
print(l[0])
print(l[7])
print(l[-1])
print(l[-2])

#методы работы со списками
numbers = [1,10, 7, 4]
numbers.append(5) #добавляет новый элемент в конец списка
print(numbers)
numbers.append(10)
print(numbers)
numbers.remove(10) #удаляет элемент из списка по значению
print(numbers)
numbers.remove(10)
print(numbers)
numbers.pop(0) #удаляет элемент по индексу
print(numbers)
#umbers.clear() #чищает список
#print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True) #reverse=True сортировка в обратном направлении
print(numbers)
numbers.append(5)
print(numbers)
print(numbers.count(5))
numbers.reverse()
print(numbers)


#функции
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

a = []
a.append(10)
a.append(11)
a.append(12)
print(a)
a.remove(12)
print(a)
a.sort(reverse=True)
print(a)
print(sum(a))

'''
найти сумму чисел от 1 до 1000 используя ф-цию sum
'''
print(sum(range(1, 1001)))