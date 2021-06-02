import os
import random

board = [[' \\ ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', '    '],
         [' 1 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 2 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 3 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 4 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 5 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 6 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 7 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 8 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' 9 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         ['10 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
         [' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' —']]

board_clear = [[' \\', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', '10 ', '    '],
               [' 1 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 2 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 3 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 4 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 5 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 6 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 7 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 8 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' 9 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               ['10 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  |'],
               [' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' — ', ' —']]


def print_board(array):
    for i in range(12):
        for j in range(12):
            print(array[i][j], end='')
        print()


def computer_turn(array, turn):
    if turn == 0:
        array[5][5] = ' O '
        print_board(board)
    else:
        while True:
            x = random.randint(1, 10)
            y = random.randint(1, 10)

            if array[x][y] == '   ':
                if 10 > x > 1:
                    if 10 > y > 1:
                        if array[x - 1][y] == " X " or array[x + 1][y] == " X " or array[x][y - 1] == " X " or \
                                array[x][y + 1] == ' X ' or array[x + 1][y + 1] == ' X ' or \
                                array[x + 1][y - 1] == ' X ' or array[x - 1][y + 1] == ' X ' or \
                                array[x - 1][y - 1] == ' X ':

                            array[x][y] = ' O '

                            if winner_o(board, turn, x, y):

                                os.system('cls')

                                print_board(board)
                                print()
                                print('O - winner !')
                                print()
                                print("Press - E to restart")
                                print("Press - Q to exit")

                                end = input()

                                while True:
                                    try:
                                        if end == 'Q' or end == 'q':
                                            os.system('cls')
                                            quit()
                                        elif end == 'E' or end == 'e':
                                            return 0
                                    except SyntaxError:
                                        print('Ooops, that not an option')
                                        print('Try again:')
                            else:
                                print_board(board)
                                break

                        elif array[x - 1][y] == " O " or array[x + 1][y] == " O " or array[x][y - 1] == " O " or \
                                array[x][y + 1] == ' O ' or array[x + 1][y + 1] == ' O ' or \
                                array[x + 1][y - 1] == ' O ' or array[x - 1][y + 1] == ' O ' or \
                                array[x - 1][y - 1] == ' O ':

                            array[x][y] = ' O '

                            if winner_o(board, turn, x, y):

                                os.system('cls')

                                print_board(board)
                                print()
                                print('O - winner !')
                                print()
                                print("Press - E to restart")
                                print("Press - Q to exit")

                                end = str(input())

                                while True:
                                    try:
                                        if end == 'Q' or end == 'q':
                                            os.system('cls')
                                            quit()
                                        elif end == 'E' or end == 'e':
                                            return 0
                                    except SyntaxError:
                                        print('Ooops, that not an option')
                                        print('Try again:')
                            else:
                                print_board(board)
                                break


def player_turn(array, row, column, turn):
    while True:

        if turn == 0:
            board[5][5] = ' X '
            return 1

        if 0 < row < 11:
            if 0 < column < 11:
                pass
        else:
            os.system('cls')
            print_board(array)
            print()
            print('Ooops, you are out of range, try again:')
            return 2

        if board[row][column] == '   ':
            if array[row - 1][column] == " O " or array[row + 1][column] == " O " or \
                    array[row][column - 1] == " O " or array[row][column + 1] == ' O ' or \
                    array[row + 1][column + 1] == ' O ' or array[row + 1][column - 1] == ' O ' or \
                    array[row - 1][column + 1] == ' O ' or array[row - 1][column - 1] == ' O ':

                board[row][column] = ' X '

                if winner_x(board, turn, row, column):

                    os.system('cls')
                    print_board(board)

                    print()
                    print('X - winner !')
                    print()
                    print("Press - E to restart")
                    print("Press - Q to exit")

                    end = input()

                    while True:
                        try:
                            if end == 'Q' or end == 'q':
                                os.system('cls')
                                quit()
                            elif end == 'E' or end == 'e':
                                return 0
                        except:
                            print('Ooops, that not an option')
                            print('Try again:')

            elif array[row - 1][column] == " X " or array[row + 1][column] == " X " or \
                    array[row][column - 1] == " X " or array[row][column + 1] == ' X ' or \
                    array[row + 1][column + 1] == ' X ' or array[row + 1][column - 1] == ' X ' or \
                    array[row - 1][column + 1] == ' X ' or array[row - 1][column - 1] == ' X ':

                board[row][column] = ' X '

                if winner_x(board, turn, row, column):

                    os.system('cls')
                    print_board(board)

                    print()
                    print('X - winner !')
                    print()
                    print("Press - E to restart")
                    print("Press - Q to exit")


                    while True:
                        end = input()
                        try:
                            if end == 'Q' or end == 'q':
                                os.system('cls')
                                quit()
                            elif end == 'E' or end == 'e':
                                return 0
                            else:
                                print('Ooops, that not an option')
                                print('Try again:')
                        except SyntaxError:
                            print('Ooops, that not an option')
                            print('Try again:')

            else:
                os.system('cls')
                print_board(board)
                print()
                print("Sorry but you able to put your figure ONLY NEAR the other figure")
                print("Try again:")
                return 2

            return 1
        else:
            os.system('cls')
            print_board(array)
            print()
            print('Ooops seems like this place is already taken or you put not a correct coordinates')
            print("Try again:")
            return 2


def winner_x(array, counter, ox, oy):
    if counter >= 9:
        
        bool_var_sum = True

        count = 0
        true_ox = ox
        true_oy = oy
        inv_ox = ox
        inv_oy = oy



        while count < 5:

            if array[ox][oy] == ' X ' and ox < 11:
                ox += 1
            elif array[inv_ox - 1][oy] == ' X ' and inv_ox > 0:
                inv_ox -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        ox = true_ox
        inv_ox = true_ox

        while count < 5:

            if array[ox][oy] == ' X ' and ox > 0:
                ox -= 1
            elif array[inv_ox + 1][oy] == ' X ' and inv_ox < 11:
                inv_ox += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        ox = true_ox
        inv_ox = true_ox

        while count < 5:

            if array[ox][oy] == ' X ' and oy < 11:
                oy += 1
            elif array[ox][inv_oy - 1] == ' X ' and inv_oy > 11:
                inv_oy -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        inv_oy = true_oy

        while count < 5:

            if array[ox][oy] == ' X ' and oy > 0:
                oy -= 1
            elif array[ox][inv_oy + 1] == ' X ' and inv_oy < 11:
                inv_oy += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        inv_oy = true_oy

        while count < 5:

            if array[ox][oy] == ' X ' and oy > 0 and ox > 0:
                ox -= 1
                oy -= 1
            elif array[inv_ox + 1][inv_oy + 1] == ' X ' and inv_ox < 11 and inv_oy < 11:
                inv_ox += 1
                inv_oy += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        ox = true_ox
        inv_oy = true_oy
        inv_ox = true_ox

        while count < 6:

            if array[ox][oy] == ' X ' and oy < 11 and ox < 11:
                ox += 1
                oy += 1
            elif array[inv_ox - 1][inv_oy - 1] == ' X ' and inv_ox > 0 and inv_oy > 0:
                inv_ox -= 1
                inv_oy -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        ox = true_ox
        inv_ox = true_ox
        inv_oy = true_oy

        while count < 6:

            if array[ox][oy] == ' X ' and oy > 0 and ox < 11:
                ox += 1
                oy -= 1
            elif array[inv_ox - 1][inv_oy + 1] == ' X ' and inv_ox > 0 and inv_oy < 11:
                inv_ox -= 1
                inv_oy += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        ox = true_ox
        inv_oy = true_oy
        inv_ox = true_ox 

        while count < 6:

            if array[ox][oy] == ' X ' and oy < 10 and ox > 0:
                ox -= 1
                oy += 1
            elif array[inv_ox + 1][inv_oy - 1] == ' X ' and inv_ox < 11 and inv_oy > 0:
                inv_ox += 1
                inv_oy -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        if counter == 100:
            os.system("cls")
            print("Draw !")
            return True
    else:
        return False


def winner_o(array, counter, ox, oy):
    if counter >= 9:

        count = 0
        true_ox = ox
        true_oy = oy
        inv_ox = ox
        inv_oy = oy

        bool_var_sum = True

        while count < 5:

            if array[ox][oy] == ' O ' and ox < 11:
                ox += 1
            elif array[inv_ox - 1][oy] == ' O ' and inv_ox > 0:
                inv_ox -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        ox = true_ox
        inv_ox = true_ox

        while count < 5:

            if array[ox][oy] == ' O ' and ox > 0:
                ox -= 1
            elif array[inv_ox + 1][oy] == ' O ' and inv_ox < 11:
                inv_ox += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        ox = true_ox
        inv_ox = true_ox

        while count < 5:

            if array[ox][oy] == ' O ' and oy < 11:
                oy += 1
            elif array[ox][inv_oy - 1] == ' O ' and inv_oy > 11:
                inv_oy -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        inv_oy = true_oy

        while count < 5:

            if array[ox][oy] == ' O ' and oy > 0:
                oy -= 1
            elif array[ox][inv_oy + 1] == ' O ' and inv_oy < 11:
                inv_oy += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        inv_oy = true_oy

        while count < 5:

            if array[ox][oy] == ' O ' and oy > 0 and ox > 0:
                ox -= 1
                oy -= 1
            elif array[inv_ox + 1][inv_oy + 1] == ' O ' and inv_ox < 11 and inv_oy < 11:
                inv_ox += 1
                inv_oy += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        ox = true_ox
        inv_oy = true_oy
        inv_ox = true_ox

        while count < 6:

            if array[ox][oy] == ' O ' and oy < 11 and ox < 11:
                ox += 1
                oy += 1
            elif array[inv_ox - 1][inv_oy - 1] == ' O ' and inv_ox > 0 and inv_oy > 0:
                inv_ox -= 1
                inv_oy -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        ox = true_ox
        inv_ox = true_ox
        inv_oy = true_oy

        while count < 6:

            if array[ox][oy] == ' O ' and oy > 0 and ox < 11:
                ox += 1
                oy -= 1
            elif array[inv_ox - 1][inv_oy + 1] == ' O ' and inv_ox > 0 and inv_oy < 11:
                inv_ox -= 1
                inv_oy += 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        count = 0
        bool_var_sum = True
        oy = true_oy
        ox = true_ox
        inv_oy = true_oy
        inv_ox = true_ox

        while count < 6:

            if array[ox][oy] == ' O ' and oy < 10 and ox > 0:
                ox -= 1
                oy += 1
            elif array[inv_ox + 1][inv_oy - 1] == ' O ' and inv_ox < 11 and inv_oy > 0:
                inv_ox += 1
                inv_oy -= 1
            else:
                bool_var = False
                bool_var_sum = bool_var_sum and bool_var

            count += 1

            if bool_var_sum is False and count == 5:
                break
            elif bool_var_sum is True and count == 5:
                return bool_var_sum

        if counter == 100:
            os.system("cls")
            print("Draw !")
            return True
    else:
        return False


def game(array):

    turns = 0

    while True:

        computer_turn(board, turns)
        
        turns += 1


        print('Your turn: row (1-10) column (1-10)')

        while True:
            try:
                myx, myy = input().split()
                myx = int(myx)
                myy = int(myy)

                case = player_turn(array, myx, myy, turns)

                if case == 1:  
                    break
                elif case == 2:
                    pass
                else:
                    return False

            except ValueError:
                print()
                print("Ooops, invalid format")
                print("Correct format: x(row) y(column)")
                print()
                print("Try again:", end=' ')

        turns += 1
        os.system("cls")


while True:

    if game(board):
        pass
    else:
        board = board_clear
