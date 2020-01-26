'''
Implementacja gry kółko i krzyżyk
Opis:

Stwórz gre w kółko i Krzyżyk dla 2 graczy. Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu, opcje takie jak imiona graczy, pomysły własne.

Przykładowa gra mogłaby wyglądać ten sposób:
'''

game_board = {
    'A1': '.', 'A2': '.', 'A3': '.',
    'B1': '.', 'B2': '.', 'B3': '.',
    'C1': '.', 'C2': '.', 'C3': '.'
}

matrix_board = [
    [' ', 'A ', ' B ', ' C'],
    [1, '.', '.', '.', ],
    [2, '.', '.', '.', ],
    [3, '.', '.', '.', ]
]

dict_row = {'A': 1, 'B': 2, 'C': 3}


def print_game_board(matrix_board):
    """
    Function prints game board on the model of matrix board 4x4
    :param matrix_board: matrix 4x4
    :return:
    prints matrix board in game
    """
    # print('  ', 'A', '  B  ', 'C')
    # print(1, f' {board["A1"]} | {board["B1"]} | {board["C1"]}')
    # print(2, f' {board["A2"]} | {board["B2"]} | {board["C2"]}')
    # print(3, f' {board["A3"]} | {board["B3"]} | {board["C3"]}')

    for row in range(len(matrix_board)):
        print()
        for col in range(len(matrix_board[row])):
            if 1 <= row <= 4 and 1 <= col <= 2:
                print(matrix_board[row][col], end=' | ')
            else:
                print(matrix_board[row][col], end=' ')
    print()


def create_matrix_board_3x3(matrix_board):
    """
    Function create matrix board 3x3 from matrix board 4x4 by removing first row and column
    :param matrix_board: matrix 4x4
    :return: matrix 3x3
    """
    new_matrix = [row[1:] for row in matrix_board[1:]]
    return new_matrix


def same_elements_in_row(matrix):
    """
    Function checks is row has the sme elements
    :param matrix: matrix 3x3
    :return: list (number of row, True or False, first element in row)
    """
    list_of_true_false = []
    for row in range(3):
        list_of_true_false.append((row, all(x == matrix[row][0] for x in matrix[row]), matrix[row][0]))
    return list_of_true_false


def change_rows_to_col(matrix):
    """
    Function changes rows to columns in matrix 3x3
    :param matrix: matrix 3x3
    :return: matrix 3x3
    """
    # for row in range(3):
    #     print()
    #     for col in range(3):
    #     #     list_true_false.append(col, all(x == matrix[col][0]) for x in martix[col])
    #         print(matrix[col][row], end=' ')
    # print()

    matrix_rows_to_col = []
    for row in range(3):
        matrix_rows_to_col_row = []
        for col in range(3):
            matrix_rows_to_col_row.append(matrix[col][row])
        matrix_rows_to_col.append(matrix_rows_to_col_row)
    return matrix_rows_to_col


def same_elements_in_col(matrix):
    """
    Function checks if in column of matrix are the same elements
    :param matrix: matrix 3x3
    :return: list (number of column, True or False, first element in row)
    """
    matrix_change = change_rows_to_col(matrix)
    return same_elements_in_row(matrix_change)


def same_elements_in_diagonal(matrix):
    """
    Function checks if in main diagonal or in antidiagonal the elements are the same
    :param matrix: matrix 3x3
    :return: list (number of row, True or False, element in diagonal)
    """
    list_true_false_main_diag = []
    list_true_false_anti_diag = []

    for row in range(3):
        list_true_false_main_diag.append((row, all(x == matrix[0][0] for x in matrix[row][row]), matrix[row][row]))
        list_true_false_anti_diag.append(
            (row, all(x == matrix[2][0] for x in matrix[row][3 - 1 - row]), matrix[row][3 - 1 - row]))

    main_true_false = []
    anti_true_false = []
    for element in range(3):
        main_true_false.append(list_true_false_main_diag[element][1])
        anti_true_false.append(list_true_false_anti_diag[element][1])

    if len(set(main_true_false)) == 1:
        return list_true_false_main_diag
    elif len(set(anti_true_false)) == 1:
        return list_true_false_anti_diag


def who_wins_row_col(list_of_true_false):
    """
    Function returns element, that won the game
    :param list_of_true_false:
    :return: string 'X' or 'O'
    """
    for element in list_of_true_false:
        if element[1] is True:
            if element[2] != '.':
                return element[2]
            else:
                continue


def main():
    dict_row = {'A': 1, 'B': 2, 'C': 3}

    print('Print game board')
    print_game_board(matrix_board)
    print()
    matrix_board_3x3 = create_matrix_board_3x3(matrix_board)

    turn = 'X'
    while '.' in game_board.values():
        print()
        move = input(f'Player {turn} mark position: ')
        if game_board[move] != '.':
        # if matrix_board_3x3[int(move[1])][dict_row[move[0]]] != '.':
            print('Put the mark on the other position.')
        else:
            game_board[move] = turn
            matrix_board[int(move[1])][dict_row[move[0]]] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            print('print_game_board: ')
            print_game_board(matrix_board)
            matrix_board_3x3 = create_matrix_board_3x3(matrix_board)
            print(matrix_board_3x3)
            same_el_rows = same_elements_in_row(matrix_board_3x3)
            same_el_col = same_elements_in_col(matrix_board_3x3)
            same_el_diag = same_elements_in_diagonal(matrix_board_3x3)
            if who_wins_row_col(same_el_rows) is not None:
                print('And the winner is:', who_wins_row_col(same_el_rows))
                break
            elif who_wins_row_col(same_el_col) is not None:
                print('And the winner is:', who_wins_row_col(same_el_col))
                break
            elif who_wins_row_col(same_el_diag) is not None:
                print('And the winner is:', who_wins_row_col(same_el_diag))
                break

    print()
    matrix_example = [['X', '.', 'X'], ['.', '.', '.'], ['O', 'O', 'O']]
    print(matrix_example)
    same_elements_row = same_elements_in_row(matrix_board_3x3)
    print(same_elements_in_row(matrix_example))
    print(change_rows_to_col(matrix_example))
    print('matrix board 3x3', matrix_board_3x3)
    who_wins_row_col(matrix_board_3x3)


if __name__ == '__main__':
    main()
