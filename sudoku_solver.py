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



board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]



