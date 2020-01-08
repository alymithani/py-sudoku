import pygame
import time
from sudoku import solve, is_complete, valid_val
from board_gen import generate

pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128,128,128)
YELLOW = (255,255,0)

class Board:
    def __init__(self, difficulty):
        self.board_array = generate(difficulty)
        self.box_array = []
        for j in range(9):
            temp_array = []
            for i in range(9):
                temp_array.append(Box(self.board_array[i][j], i, j))
            self.box_array.append(temp_array)
        
    def draw(self, window):
        pygame.draw.line(window, BLACK, (0,0), (630,0), 6)
        pygame.draw.line(window, BLACK, (0,210), (630,210), 6)
        pygame.draw.line(window, BLACK, (0,420), (630,420), 6)
        pygame.draw.line(window, BLACK, (0,630), (630,630), 6)
        pygame.draw.line(window, BLACK, (0,0), (0,630), 6)
        pygame.draw.line(window, BLACK, (210,0), (210,630), 6)
        pygame.draw.line(window, BLACK, (420,0), (420,630), 6)
        pygame.draw.line(window, BLACK, (630,0), (630,630), 6)
        for i in range(9):
            for j in range(9):
                self.box_array[i][j].draw(window)
    
    def select(self, position):
        column = int(position[0]/70)
        row = int(position[1]/70)
        if 0 <= row < 9 and 0 <= column < 9:
            if self.box_array[row][column].value == 0:
                for i in range(9):
                    for j in range(9):
                        self.box_array[i][j].selected = False
                self.box_array[row][column].selected = True
    
    def set_temp(self, key):
        for i in range(9):
            for j in range(9):
                if self.box_array[i][j].selected == True:
                    self.box_array[i][j].temp_value = key
    
    def set_val(self):
        value = 0
        for i in range(9):
            for j in range(9):
                if self.box_array[i][j].selected == True:
                    value = self.box_array[i][j].temp_value
                    row = i
                    column = j
        if value == 0:
            return 0
        else:
            if not valid_val(self.board_array, row, column, value):
                self.box_array[row][column].temp_value = 0
                return -20
            self.board_array[row][column] = value
            if solve(self.board_array):
                self.box_array[row][column].value = value
                for i in range(9):
                    for j in range(9):
                        self.board_array[i][j] = self.box_array[i][j].value
                self.box_array[row][column].selected = False
                return 100
            else:
                self.box_array[row][column].temp_value = 0
                for i in range(9):
                    for j in range(9):
                        self.board_array[i][j] = self.box_array[i][j].value
                return -20


class Box:
    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column
        self.temp_value = 0
        self.selected = False
    
    def draw(self, window):
        x_position = self.row * 70
        y_position = self.column * 70
        pygame.draw.rect(window, BLACK, (x_position, y_position, 70, 70), 2)
        if self.value != 0:
            font = pygame.font.SysFont('Comic Sans MS', 50)
            text = font.render(str(self.value), 1, BLACK)
            window.blit(text, (x_position + 24, y_position + 21))
        elif self.temp_value != 0:
            font = pygame.font.SysFont('Comic Sans MS', 25)
            text = font.render(str(self.temp_value), 1, GRAY)
            window.blit(text, (x_position + 10, y_position + 10))
        if self.selected:
            pygame.draw.rect(window, YELLOW, (x_position + 3, y_position + 3, 64, 64), 4)

def draw_window(window, game_board, score, current_time):
    window.fill(WHITE)
    game_board.draw(window)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    text = font.render("Score: " + str(score), 1, BLACK)
    window.blit(text, (20,650))
    formatted_time = str(int(current_time//60)) + ":" + "{:0>2d}".format(int(current_time%60))
    text = font.render("Time: "+ formatted_time, 1, BLACK)
    window.blit(text, (480,650))
    pygame.display.update()

def get_difficulty():
    window =  pygame.display.set_mode((600, 250))
    pygame.display.set_caption("py-sudoku")
    window.fill(WHITE)
    pygame.draw.line(window, BLACK, (0,100), (600,100), 6)
    pygame.draw.line(window, BLACK, (150,100), (150,250), 6)
    pygame.draw.line(window, BLACK, (300,100), (300,250), 6)
    pygame.draw.line(window, BLACK, (450,100), (450,250), 6)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    text = font.render("Select a Difficulty...", 1, BLACK)
    window.blit(text, (180,40))
    font = pygame.font.SysFont('Comic Sans MS', 25)
    text = font.render("Easy", 1, BLACK)
    window.blit(text, (55,175))
    text = font.render("Medium", 1, BLACK)
    window.blit(text, (195,175))
    text = font.render("Hard", 1, BLACK)
    window.blit(text, (355,175))
    text = font.render("Very Hard", 1, BLACK)
    window.blit(text, (485,175))
    pygame.display.update()
    difficulty = ''
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[1] > 100:
                    if 0 < position[0] < 150:
                        difficulty = 'easy'
                    elif 150 < position[0] < 300:
                        difficulty = 'medium'
                    elif 300 < position[0] < 450:
                        difficulty = 'hard'
                    else:
                        difficulty = 'very_hard'
                    running = False
    return difficulty

if __name__ == "__main__":
    difficulty = get_difficulty()
    running = False
    if difficulty != '':
        window =  pygame.display.set_mode((630, 690))
        pygame.display.set_caption("py-sudoku")
        game_board = Board(difficulty)
        start_time = time.time()
        score = 0
        key = 0
        running = True
    win = False
    while running:
        current_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_board.select(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if key != 0:
                    game_board.set_temp(key)
                    key = 0
                if event.key == pygame.K_BACKSPACE:
                    game_board.set_temp(0)
                if event.key == pygame.K_RETURN:
                    score += game_board.set_val()
                    if is_complete(game_board.board_array):
                        finish_time = time.time() - start_time
                        win = True
                        running = False
        draw_window(window, game_board, score, current_time)
    if win:
        formatted_finish_time = str(int(finish_time//60)) + ":" + "{:0>2d}".format(int(finish_time%60))
        print('Game Completed in ' + formatted_finish_time + '! Score: ' + str(score) + '.')