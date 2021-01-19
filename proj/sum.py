def game():
    matrix = [['-' for j in range(3)] for i in range(3)]
    pobeda = False
    hod_x = True
    print_matrix(matrix)
    stopgame = False
    while stopgame != True:
        hod_x = hod(matrix, hod_x)
        pobeda = is_pobeda(matrix)
        if(pobeda == True):
            stopgame = True
        if((two_to_one_dimension_matrix(matrix)).count('-') == 0):
            stopgame = True


    if(pobeda == True):
        if(hod_x==False):
            print('Победили крестики')
        else:
            print('Победили нолики')
    else:
        print('Ничья')


def is_pobeda(m):
    p = False;
    one_dimension_matrix = two_to_one_dimension_matrix(m)
    p = check_vertical(one_dimension_matrix, p)
    p = check_horizontal(m, p)
    p = check_diagonal(one_dimension_matrix, p)
    return p


def two_to_one_dimension_matrix(m):
    one_dimension_matrix = []
    for row in m:
        for elem in row:
            one_dimension_matrix.append(elem)
    return one_dimension_matrix


def check_diagonal(one_dimension_matrix, p):
    sub = one_dimension_matrix[0::4]
    if (sub[0] == sub[1] == sub[2] and sub[0] != '-'):
        p = True
    sub = one_dimension_matrix[2:7:2]
    if (sub[0] == sub[1] == sub[2] and sub[0] != '-'):
        p = True
    return p


def check_horizontal(m, p):
    for row in m:
        if (row[0] == row[1] == row[2] and row[0] != '-'):
            p = True
    return p


def check_vertical(one_dimension_matrix, p):
    for i in range(0, 3):
        sub = one_dimension_matrix[i::3]
        # print(sub)
        if (sub[0] == sub[1] == sub[2] and sub[0] != '-'):
            p = True
    return p


def hod(m, hodit_x):
    x = hodit_x
    if(x == True):
        print("\033[33m",end='')
        index = input('ходят крестики, укажите индекс ячейки: ')
        flag_int = False
        flag_len = False
        flag_int = proverka_int(index)
        flag_len = proverka_len(index)

        if (flag_int and flag_len == True):
            if(m[int(index[0])][int(index[1])] == '-'):
                m[int(index[0])][int(index[1])] = 'x'
                x = False
            else:
                print("\033[31m", end='')
                print('клеточка занята, повторите ход')
                x = True
        else:
            print("\033[31m", end='')
            print('неправильно введен индекс клеточки')
            x = True
    else:
        print("\033[33m", end='')
        index = input('ходят нолики, укажите индекс ячейки: ')
        flag_int = False
        flag_len = False
        flag_int = proverka_int(index)
        flag_len = proverka_len(index)

        if (flag_int and flag_len == True):
            if (m[int(index[0])][int(index[1])] == '-'):
                m[int(index[0])][int(index[1])] = '0'
                x = True
            else:
                print("\033[31m", end='')
                print('клеточка занята, повторите ход')
                x = False
        else:
            print("\033[31m", end='')
            print('неправильно введен индекс клеточки')
            x = False
    print_matrix(m)
    return x


def proverka_len(index):
    flag = False
    try:
        if (len(index) > 1):
            flag = True
        else:
            flag = False
    except Exception:
        flag = False
    return flag


def proverka_int(index):
    flag = False
    i=-2
    try:
        i=int(index)
        flag = True
    except ValueError:
        flag = False
    if(i>-1 and i<23):
        flag = True
    else:
        flag = False
    return flag


def print_matrix(m):
    print("\033[34m")
    print('  ','0','1','2')
    i=-1
    for row in m:
        i=i+1
        print("\033[34m",i,end = ' ' )
        for elem in row:
            print("\033[33m{}".format(elem),end = ' ')
        print()
#
game()

