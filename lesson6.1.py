#матрицы
numbers = [1,2,3,4,5,6] #одномерный массив (список)
#          0 1 2 3 4 5

#3x5
matrix = [
#    0 1 2 3 4
    [1,2,3,4,5], #0
    [6,7,8,9,0], #1
    [4,2,3,4,5]  #2
]
print(matrix[1][3])

for i in numbers:
    print(i)


max_element = matrix[0][0]
for row in matrix:
    for col in row:
        if col > max_element:
            max_element = col
print(max_element)

#print(max(matrix))

b = [[
        [1, 2, 13],
        [1, 2, 3]
    ],[
        [1, 2, 3],
        [1, 2, 3]
    ]
]
print(b[0][0][2])


#найти произведение элементов главной диагонали

#5x5 (квадратная)
c = [
 #   0 1 2 3 4
    [1,2,3,4,5], #0
    [3,4,3,2,3], #1
    [1,2,3,4,5], #2
    [3,4,3,2,3], #3
    [3,4,3,2,3], #4
]


#range(4) 0 1 2 3
#range(1, 5) 1 2 3 4
#range(4, 10, 2) 4 6 8
p = 1
for row in range(len(c)):
    for column in range(len(c)):
        if row == column:
            p = p * c[row][column] #p = 1 * 1 = 1   p =  1 * 4 = 4  p=4 * 3 = 12    p = 12 * 2 = 24     p  = 24 * 3 = 72
print(p)


