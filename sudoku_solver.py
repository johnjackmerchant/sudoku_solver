#prints board
def print_board(board):
    for i in range(len(board)):
        print(board[i])

#finds empty cells
def find_empty(board):
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if board[row_index][column_index] == 0:
                return row_index, column_index

#determines if number can go in row
def is_row_valid(board, row_index, number):
    for cell in board[row_index]:
        if cell == number:
            return False
    return True

#determines if number can go in column
def is_column_valid(board, column_index, number):
    for row_index in range(len(board)):
        if board[row_index][column_index] == number:
            return False
    return True

#determines if number can go in box
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

#determines if number can go in a cell
def is_valid(board, row_index, column_index, number):
    if is_row_valid(board, row_index, number) and is_column_valid(board, column_index, number) and is_box_valid(board, row_index, column_index, number):
        return True
    else:
        return False

#solves board by finding empty cell and calling is_valid
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

#determines if entered board has conflicting clues
def is_board_valid(board):
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if board[row_index][column_index] == 0:
                continue
            else:
                temp = board[row_index][column_index]
                board[row_index][column_index] = 0
                cell_check = is_valid(board, row_index, column_index, temp)
                board[row_index][column_index] = temp
                if cell_check == True:
                    continue
                else:
                    return False

    return True

#user instructions
print("Enter 9 digits per row, using 0 for empty cells")

#gets rows from user and validates rows
entered_rows = []
for row in range(1,10):
    i = 0
    while i != 1:
        user_row = (input(f"Enter row {str(row)}: "))
        if len(user_row) == 9:
            valid_digits = True
            for num in user_row:
                if not num in ("0123456789"):
                    valid_digits = False
                    print("Each row may only contain digits 0-9")
                    break 
        else:
            print("Each row may only contain 9 digits")
            continue        
        if valid_digits == True:
            clean_row = [int(num) for num in user_row]
            entered_rows.append(clean_row)
            i += 1

#solves board if valid       
if is_board_valid(entered_rows):
    if solve(entered_rows):
        print("Puzzle solved!")
        print_board(entered_rows)
    else:
        print("No solution found")
else:
    print("Entered board has conflicting clues")
