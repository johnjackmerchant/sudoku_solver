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

print(is_column_valid(board, 2, 7))

