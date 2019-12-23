def print_board(board):
    # Prints 9x9 array of integers representing the sudoku board
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = ' ')
        print()

def is_complete(board):
    # Returns true if there are no blank spaces left on the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def next_blank(board):
    # returns the index of the next blank space on the board
    for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j

def valid_row(board, i, val):
    # returns true if a given value can be placed on a given row on the board
    for j in range(9):
        if board[i][j] == val:
            return False
    return True

def valid_column(board, j, val):
    # returns true if a given value can be placed on a given column on the board
    for i in range(9):
        if board[i][j] == val:
            return False
    return True

def valid_box(board, i, j, val):
    # returns true if a given value can be placed in a 3x3 box on the board
    x = (i//3)*3
    y = (j//3)*3
    for i in range (x, x+3):
        for j in range(y, y+3):
            if board[i][j] == val:
                return False
    return True

def valid_val(board, i, j, val):
    # returns true if a given value can be placed on the board given its row, column and 3x3 box
    return valid_row(board, i, val) and valid_column(board, j, val) and valid_box(board, i, j, val)

def solve(board):
    # returns true if there exists a solution to the given board and completes it
    if is_complete(board):
        return True
    i, j = next_blank(board)
    for val in range(1,10):
        if valid_val(board, i, j, val):
            board[i][j] = val
            if solve(board):
                return True
            board[i][j] = 0
    return False

def open_file(file):
    # returns a 9x9 array of integers representing a sudoku board from a given input file
    f = open(file)
    board = []
    for i in range(9):
        board.append(f.readline().split())
    for i in range(9):
        for j in range(9):
            board[i][j] = int(board[i][j])
    return board

if __name__ == "__main__":
    for i in range(1, 4):
        board = open_file("./examples/board{0}.txt".format(i))
        if solve(board):
            print_board(board)
        else:
            print("There is no possible solution.")
        print()
