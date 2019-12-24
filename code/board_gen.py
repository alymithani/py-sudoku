import sudoku

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

def reflect_x(board):
    for i in range(5):
        for j in range(9):
            temp = board[i][j]
            board[i][j] = board[8-i][j]
            board[8-i][j] = temp

def reflect_y(board):
    for i in range(9):
        for j in range(5):
            temp = board[i][j]
            board[i][j] = board[i][8-j]
            board[i][8-j] = temp

def rotate(board):
    # rotate clockwise 90 degrees

if __name__ == "__main__":
    board = open_file("./seeds/easy.txt")
    reflect_y(board)
    sudoku.print_board(board)