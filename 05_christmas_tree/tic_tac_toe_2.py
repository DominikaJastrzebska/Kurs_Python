# def create_board():
#     # print('  A', '  B  ', 'C', end=' ')
#     print()
#     for i in range(0, 4):
#         if i == 0:
#             print(' ', 'A  ', 'B  ', 'C', end=' ')
#             print()
#         else:
#             print(i, end=' ')
#         for j in range(3):
#             if i == 0:
#                 pass
#             else:
#                 if j < 2:
#                     print('. | ', end='')
#                 else:
#                     print('.')
#
#
# def who_wins():
#     pass
#
#
# create_board()
#
#
# def transform_move_to_read_matrix_value(move):
#     two = []
#     for i in range(len(move)):
#         two.append(move[i])
#
#     return two
#
# print(transform_move_to_read_matrix_value('A1'))
#
# matrix_board = [
#     [' ', 'A ', ' B ', ' C'],
#     [1, '.', '.', '.', ],
#     [2, '.', '.', '.', ],
#     [3, '.', '.', '.', ]
# ]
#
# dict_row = {'A': 1, 'B': 2, 'C': 3}
# turn = 'B2'
#
# matrix_board[1][1] = 'x'
# matrix_board[dict_row[turn[0]]][int(turn[1])] = 'y'
#
# print(matrix_board)
# print('------------')
#
#
# matrix_board_2 = [
#     [' ', 'A ', ' B ', ' C'],
#     [1, '.', '.', '.', ],
#     [2, '.', '.', '.', ],
#     [3, '.', '.', '.', ]
# ]
#
# new_matrix = [row[1:] for row in matrix_board_2[1:]]
# print(new_matrix)

# def create_board():
#     """
#     Function create empty board of tic tac toe game
#     :return:
#     print board
#     """
#     # print('A', '  B  ', 'C', end=' ')
#     # print()
#     # for i in range(3):
#     #     for j in range(3):
#     #         if j < 2:
#     #             print('. | ', end='')
#     #         else:
#     #             print('.')
#     # print('  A', '  B  ', 'C', end=' ')
#
#     for i in range(0, 4):
#         if i == 0:
#             print(' ', 'A  ', 'B  ', 'C', end=' ')
#             print()
#         else:
#             print(i, end=' ')
#         for j in range(3):
#             if i == 0:
#                 pass
#             else:
#                 if j < 2:
#                     print('. | ', end='')
#                 else:
#                     print('.')



matrix_board_3x3 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]


def same_elements_in_row(matrix):
    list_of_true_false = []
    for row in range(3):
        list_of_true_false.append((row, all(x == matrix[row][0] for x in matrix[row]), matrix[row][0]))
    return list_of_true_false


def who_wins_row_col(list_of_true_false):
    for element in list_of_true_false:
        # print(element[1])
        if element[1] is True:
            if element[2] != '.':
                return element[2]
            else:
                continue


def change_rows_to_col(matrix):
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
    matrix_change = change_rows_to_col(matrix)
    print(matrix_change)
    print(same_elements_in_row(matrix_change))
    return same_elements_in_row(matrix_change)


def same_elements_in_diagonal(matrix):
    list_true_false_main_diag = []
    list_true_false_anti_diag = []

    for row in range(3):
        list_true_false_main_diag.append((row, all(x == matrix[0][0] for x in matrix[row][row]), matrix[row][row]))
        list_true_false_anti_diag.append((row, all(x == matrix[2][0] for x in matrix[row][3-1-row]), matrix[row][3-1-row]))

    main_true_false = []
    anti_true_false = []
    for element in range(3):
        main_true_false.append(list_true_false_main_diag[element][1])
        anti_true_false.append(list_true_false_anti_diag[element][1])

    if len(set(main_true_false)) == 1:
        return list_true_false_main_diag
    elif len(set(anti_true_false)) == 1:
        return list_true_false_anti_diag


def main():
    matrix_board_3x3 = [['X', 'O', 'O'], ['.', '.', '.'], ['O', 'O', 'X']]
    for row in range(3):
        print(matrix_board_3x3[row])
    same_el_row = same_elements_in_row(matrix_board_3x3)
    print(same_el_row)
    print(who_wins_row_col(same_el_row))
    # same_el_col = same_elements_in_col(matrix_board_3x3)
    # print(same_el_col)
    # print(who_wins_row_col(same_el_col))
    # print(same_elements_in_diagonal(matrix_board_3x3))
    # same_elements_in_diagonal(matrix_board_3x3)


if __name__ == '__main__':
    main()