def print_board(board):
    for i in range(len(board)):
        print(board[i])


def find_empty(board):
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if board[row_index][column_index] == 0:
                return row_index, column_index


def is_row_valid(board, row_index, number):
    for cell in board[row_index]:
        if cell == number:
            return False
    return True


def is_column_valid(board, column_index, number):
    for row_index in range(len(board)):
        if board[row_index][column_index] == number:
            return False
    return True


def is_box_valid(board, row_index, column_index, number):
    if row_index < 3:
        row_start = 0
    elif row_index < 6:
        row_start = 3
    else:
        row_start = 6

    if column_index < 3:
        column_start = 0
    elif column_index < 6:
        column_start = 3
    else:
        column_start = 6

    for row in range(row_start, row_start + 3):
        for column in range(column_start, column_start + 3):
            if board[row][column] == number:
                return False

    return True


def is_valid(board, row_index, column_index, number):
    if is_row_valid(board, row_index, number) and is_column_valid(board, column_index, number) and is_box_valid(board, row_index, column_index, number):
        return True
    else:
        return False


def solve(board):
    empty_position = find_empty(board)
    if empty_position is None:
        return True

    row_index, column_index = empty_position

    for num in range(1,10):
        if is_valid(board, row_index, column_index, num):
            board[row_index][column_index] = num
            if solve(board):
                return True
            else:
                board[row_index][column_index] = 0            

    return False 



board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

solve(board)

print_board(board)

