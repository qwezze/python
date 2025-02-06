#list(списки)

numbers = [1,2,3,4,5,10,23]
print(numbers[1])
print(sum((numbers)))
print(min(numbers))
print(max(numbers))
print(len(numbers))


numbers.remove(23)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.clear()
print(numbers)
numbers.append(1)


#кортеж (tuple)

b = (1,2,3,4,5,6)


a1 = [1,2,3]
a1[2] = 5
print(a1)
a2 = (1,2,3)
#a2[2] = 5
print(a2)



c = (1,2,3,4,5,6)
d = list(c) #[1,2,3,4,5,6]
d[5] = 7
d1 = tuple(d) #(1,2,3,4,5,7)
print(d1)


#словари (dict (dictionary))
users = {'login': 'user1', 'password': '12345'}
print(users['login'])
users['age'] = 20
print(users)


users = [
    {'login': 'user1', 'password': '12345'}, #0
    {'login': 'user2', 'password': '123456'}, #1
    {'login': 'user3', 'password': '123457'}, #2
    {'login': 'user4', 'password': '123458'},
]
print(users[2]['password'])

#set(множества)

d = {1, 2, 3, 4, 4, 4}
print(d)
d.add(5)
print(d)
d.remove(3)
print(d)
d.add(1)
print(d)
#d.clear()
#print(d)

if 1 in d:
    print('Ok')


set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))





users = ['user1', 'user2', 'user1', 'user3']
print(list(set(users)))
