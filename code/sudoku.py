def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = ' ')
        print()

def is_complete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def next_blank(board):
    for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j

def valid_row(board, i, val):
    for j in range(9):
        if board[i][j] == val:
            return False
    return True

def valid_column(board, j, val):
    for i in range(9):
        if board[i][j] == val:
            return False
    return True

def valid_box(board, i, j, val):
    x = (i//3)*3
    y = (j//3)*3
    for i in range (x, x+3):
        for j in range(y, y+3):
            if board[i][j] == val:
                return False
    return True

def valid_val(board, i, j, val):
    return valid_row(board, i, val) and valid_column(board, j, val) and valid_box(board, i, j, val)

def solve(board):
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
    f = open(file)
    board = []
    for i in range(9):
        board.append(f.readline().split())
    for i in range(9):
        for j in range(9):
            board[i][j] = int(board[i][j])
    return board

if __name__ == "__main__":
    board = open_file("./board1.txt")
    if solve(board):
        print_board(board)
    else:
        print("There is no possible solution.")