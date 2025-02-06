#for
'''s = 'hello world   '
i = 0
for char in s: #char='h'    char='e'     ...    char='d'
    #print(char)
    if char == ' ': #'h' == ' ' (False)
        i += 1
print(i)'''

'''
range(1, 101) сформирует последовательность 1,2,3,4,...,100
'''
for i in range(1, 101, 2):
    print(i)

'''
100,99,98,...,0
'''

for i in range(100, -1, -1):
    print(i)


for i in range(1, 11): #i=1 i=2 i=3
    for j in range(1, 11):#i=3 j=1,2,3,4,5,6,7,8,9,10
        print(i,'*',j, '=',i * j, end='\t')
    print()

'''
вывести числа в диапазоне от 10 до 1000, которые делятся на 5 и на 6
'''
for i in range(10, 1001):
    if i % 5 == 0 and i % 6 == 0:
        print(i)