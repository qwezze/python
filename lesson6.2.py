matrix = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]
for i in matrix:
    print(*i)


play = '0'
win = False
while True:
    row,column =map(int, input(f'Ход {play}. Введите строку и столбец: ').split()) #'0 1' -> ['0', '1']
    if row > 2 or column > 2:
        print('Error')
        continue
    if matrix[row][column] != '.':
        print('Error')
        continue
    if play == '0':
        matrix[row][column] = '0'
        play = 'x'
    elif play == 'x':
        matrix[row][column] = 'x'
        play = '0'

    for i in matrix:
        print(*i)

    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == '0':
            win = '0'
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == '0':
            win = '0'
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == '0':
        win = '0'
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == '0':
        win = '0'

    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == 'x':
            win = 'x'
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == 'x':
            win = 'x'
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'x':
        win = 'x'
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'x':
        win = 'x'

    if win == '0':
        print('Выиграл 0')
        break
    if win == 'x':
        print('Выиграл x')
        break

    h = False
    for row1 in matrix:
        for col1 in row1:
            if col1 == '.':
                h = True
    if h == False:
        print('Ничья')
        break
with open('matrix.txt', 'w') as f:
    for i in matrix: #i=['.', '.', '.'] -> . . .
        f.write(' '.join(i) + '\n')

#if matrix[0][0] == matrix[0][1] == matrix[0][2] == '0' or matrix[1][0] == matrix[1][1] == matrix[1][2] == '0' or matrix[2][0] == matrix[2][1] == matrix[1][2] == '0':



a = 'a.b.c'
print(a.split('.')) #['a','b','c']

b = ['a', 'b', 'c']
print('.'.join(b)) #a.b.c
