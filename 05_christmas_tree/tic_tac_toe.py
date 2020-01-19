'''
Implementacja gry kółko i krzyżyk
Opis:

Stwórz gre w kółko i Krzyżyk dla 2 graczy. Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu, opcje takie jak imiona graczy, pomysły własne.

Przykładowa gra mogłaby wyglądać ten sposób:
'''


def create_board():
    """
    Function create empty board of tic tac toe game
    :return:
    print board
    """
    print('A', '  B  ', 'C', end=' ')
    print()
    for i in range(3):
        for j in range(3):
            if j < 2:
                print('. | ', end='')
            else:
                print('.')


game_board = {
    'A1': '.', 'A2': '.', 'A3': '.',
    'B1': '.', 'B2': '.', 'B3': '.',
    'C1': '.', 'C2': '.', 'C3': '.'
}


def print_game_board(board):
    print('  ', 'A', '  B  ', 'C')
    print(1, f' {board["A1"]} | {board["B1"]} | {board["C1"]}')
    print(2, f' {board["A2"]} | {board["B2"]} | {board["C2"]}')
    print(3, f' {board["A3"]} | {board["B3"]} | {board["C3"]}')


# def print_game_board_2():
#     BOARD_ROWS = [' ', 'A', 'B', 'C']
#     BOARD_COLUMNS = [' ', 1, 2, 3]
#     board = []
#     for row_el in BOARD_ROWS:
#         board_row = []
#         for col_el in BOARD_COLUMNS:
#             if board[0]:
#                 board_row.append(row_el)
#             else:
#                 board_row.append('.')
#         board.append(board_row)
#     return board
#
#
# print(print_game_board_2())


# rozgrywka
# turn = 'X'
# while '.' in game_board.values():
#     print()
#     move = input(f'Player {turn} mark position: ')
#     if game_board[move] != '.':
#         print('Put the mark on the other position.')
#     else:
#         game_board[move] = turn
#         if turn == 'X':
#             turn = 'O'
#         else:
#             turn = 'X'
#         print_game_board(game_board)
#     # win_row(game_board)


def tic_tac_toe_matrix():
    """
    Function create tic tac toe matrix on the model of print_game_board(board) function
    :return:
    """
    tic_tac_toe_matrix = []
    for row in range(3):
        matrix_row = []
        for col in range(3):
            matrix_row.append('.')

        tic_tac_toe_matrix.append(matrix_row)
    return tic_tac_toe_matrix


print('tic tac toe:', tic_tac_toe_matrix())


dict_col = {'A': 0, 'B': 1, 'C': 2}
dict_row = {1: 0, 2: 1, 3: 2}

print()


def row_wins(matrix):
    list_of_true_false = []
    for row in range(3):
        list_of_true_false.append((row, all(x == matrix[row][0] for x in matrix[row]), matrix[row][0]))
    return list_of_true_false


def col_wins(matrix):
    list_true_false = []
    for row in range(3):
        print()
        for col in range(3):
        #     list_true_false.append(col, all(x == matrix[col][0]) for x in martix[col])
            print(matrix[col][row], end=' ')


def main():
    print('Create board: ')
    create_board()
    print('Print game board')
    print_game_board(game_board)
    print('Print tic tac toe matrix on the model of print_game_board(game_board) function')
    print(tic_tac_toe_matrix())
    for row in range(3):
        print()
        for col in range(3):
            print(tic_tac_toe_matrix[row][col], end=' ')

    matrix_example = [['X', '.', 'X'], ['v', 'v', 'v'], ['.', 'm', '.']]
    print(row_wins(matrix_example))
    col_wins(matrix_example)


if __name__ == '__main__':
    main()
