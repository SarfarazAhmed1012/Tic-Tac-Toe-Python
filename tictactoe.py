import pygame, sys, numpy as np

pygame.init()

# Creating the screen
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # SCREEN SIZE
pygame.display.set_caption('Tic Tac Toe')  # CAPTION
screen.fill(BG_COLOR)  # SCREEN COLOR

# BOARD
board = np.zeros((BOARD_ROWS, BOARD_COLS))



# CREATING THE LINES
# Below is a simple line
# pygame.draw.line(screen, RED, (10, 10), (300, 300), 5) # here arguements are screen, line color, staring and ending position, and line width

def draw_lines():
    # horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


# function that draws figures on screen
def draw_figs():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # for player 1
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:  # for player 2 (squares)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

#
# function to mark the squares
def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):  # will return TRUE if the square is available
    if board[row][col] == 0:
        return True
    else:
        return False

# this function checks all the boxes if they are full or not trough looping
def is_board_full():
    for rows in range(BOARD_ROWS):
        for cols in range(BOARD_COLS):
            if board[rows][cols] == 0:
                return False
    return True


def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):  # loop through all the rows
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win check
    for row in range(BOARD_ROWS): # loop through all the cols
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(col, player)
            return True

    #  asc diagonals win check

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonals win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True



def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


#     LETS CHECK IF THE MIDDLE SQUARE IS AVAILABLE
# print(available_square(1, 1)) # True
# mark_square(1, 1, 2)
# print(available_square(1, 1))   # False

# for row in range(BOARD_ROWS):
#   for col in range(BOARD_COLS):
#       mark_square(row, col, 1)


draw_lines()

player = 1
game_over = False
# MAINLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # for x coordinate
            mouseY = event.pos[1]  # for y coordinate
            # To link our console board to our screen board, we need to access on x and y coordinates.

            clicked_row = int(mouseY // 200)  # 200 is the length of each square
            clicked_col = int(mouseX // 200)

            print(clicked_row)
            print(clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2  # updating the turn of player 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1  # updating the turn of player 1
                draw_figs()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    pygame.display.update()  # will not change the display until updated
