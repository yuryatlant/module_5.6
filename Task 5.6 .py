#моя первая игра: крестики нолики

matrix = [
    [' ',   1,   2,   3], 
    [1  , '_', '_', '_'],
    [2  , '_', '_', '_'],
    [3  , '_', '_', '_'], 
]

def vivod_matrici(L):
    for i in range(len(matrix)):
        print(*matrix[i])

#    for i in range(4):  
#        for j in range(4):  
#            print(L[i][j], end=" ")
#        print()

def vvod_data(L):
    while True:
        row = input('введите ряд:')
        column = input('введите столбец:')
        if not (row.isdigit() and column.isdigit()):
            print("нужно ввести цифры")
            continue
        x,y = int(row),int(column)
        if not ((0<x<4) and (0<y<4)):
            print("нет такого ряда/столбца!")
            continue
        if L[x][y] != '_':
            print("место уже занято значением")
            continue
        break
    return x,y

def proverka(L,znak):
    def rovno (a,b,c,d):
        if a==d and b==d and c==d:
            return True
    for n in range(1,4):
        if rovno(L[1][n],L[2][n],L[3][n],znak) or \
        rovno(L[n][1],L[n][2],L[n][3],znak) or \
        rovno(L[1][1],L[2][2],L[3][3],znak) or \
        rovno(L[3][1],L[2][2],L[1][3],znak):
            return True
    return False
    
print("                    Игра крестики-нолики             ")
print("     Подчеркнутые поля предназаначены для ввода значений")
print("Для ввода, пожалуйста, введите ряд и колонку нужной клетки(поля)")
print()
count = 0
while True:
    vivod_matrici (matrix)
    kletka = vvod_data(matrix)
    if count%2 == 0:
        matrix[kletka[0]][kletka[1]] = 'x'
        zn = 'x'
    else:
        matrix[kletka[0]][kletka[1]] = '0'
        zn ='0'
    if count == 8: 
        print ("Ничья")
        break
    if proverka(matrix,zn):
        print(f"winner {zn}")
        break

    count += 1
    