import random
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
    # rotates counter-clockwise
    rotated_board = []
    for i in range(9):
        array = []
        for j in range(9):
            array.append(board[j][8-i])
        rotated_board.append(array)
    return rotated_board

def random_array():
    array = [0]
    while (len(array) != 10):
        x = random.randint(1,9)
        if (x not in array):
            array.append(x)
    return array

def generate(difficulty):
    try:
        board = open_file("./seeds/{0}.txt".format(difficulty))
    except:
        print('Invalid difficulty selected.')
        return 0
    x = random.randint(0,1)
    if (x):
        reflect_x(board)
    x = random.randint(0,1)
    if (x):
        reflect_y(board)
    x = random.randint(0,3)
    for i in range(x):
        board = rotate(board)
    array = random_array()
    for i in range(9):
        for j in range(9):
            board[i][j] = array[board[i][j]]
    return board

if __name__ == "__main__":
    board = generate("very_hard")
    assert board
    sudoku.print_board(board)
    print()
    assert sudoku.solve(board)
    sudoku.print_board(board)