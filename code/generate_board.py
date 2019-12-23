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

