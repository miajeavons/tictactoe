import pygame
import sys

pygame.init()

# Section 1: board set up 
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe!")
WIN_SIZE = 500
CELL_SIZE = WIN_SIZE // 3
# font 
font = pygame.font.Font(None, 32)

# variables for while loop
click = False
current_pos = []
player = 1

# Images Scaled 
# https://www.youtube.com/watch?v=IL_PMGVxEUY 
# I took the pygame.image.load function and scaled the image in reference to my window and cell size
BOARD = pygame.transform.scale(pygame.image.load("Board.png"), ([WIN_SIZE] * 2))
X_PNG = pygame.transform.scale(pygame.image.load("X.png"), ([CELL_SIZE] * 2))
O_PNG = pygame.transform.scale(pygame.image.load("O.png"), ([CELL_SIZE] * 2))
BG_COLOUR = (0,0,0)

# graphical board with no values
graphical_board = [[0, 0, 0], 
                   [0, 0, 0], 
                   [0, 0, 0]]


def check_win(): # win probabilities
    for i in range(3):
        if graphical_board[i][0] == graphical_board[i][1] == graphical_board[i][2] != 0:
            return True  # row win
        if graphical_board[0][i] == graphical_board[1][i] == graphical_board[2][i] != 0:
            return True  # column win
    if graphical_board[0][0] == graphical_board[1][1] == graphical_board[2][2] != 0:
        return True  # diagonal win
    if graphical_board[0][2] == graphical_board[1][1] == graphical_board[2][0] != 0:
        return True  # diagonal win
    return False

run = True
while run:
# event handler - exits the game
    # https://www.youtube.com/watch?v=vpodgih0X0Q 
    # I took the position of the mouse being clicked by printed on the screen who wins as well as adapting the code into mine using CELL_SIZE instead of a numerical value. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# shows click can process the event
        if event.type == pygame.MOUSEBUTTONDOWN and not click:
            click = True
        if event.type == pygame.MOUSEBUTTONUP and click:
            click = False
# take position where mouse was clicked
            current_pos = pygame.mouse.get_pos()
            cell_x = current_pos[0] // CELL_SIZE
            cell_y = current_pos[1] // CELL_SIZE
            if graphical_board[cell_y][cell_x] == 0:
                graphical_board[cell_y][cell_x] = player
                player *= -1  # if player1 is originally 1, player2 would be -1

# prints who wins on the screen 
            if check_win():
                text = font.render(f"Player {1 if player == -1 else 2} wins!", True, (255, 87, 51))
                SCREEN.blit(text, (240,20))
                pygame.display.update()
                pygame.time.delay(1500)
                run = False 

    SCREEN.fill(BG_COLOUR)
    SCREEN.blit(BOARD, (64, 64))

# adds the images of X and O
   
    for row in range(3):
        for col in range(3):
            if graphical_board[row][col] == 1:
                SCREEN.blit(X_PNG, (col * CELL_SIZE + 60, row * CELL_SIZE + 70))
            elif graphical_board[row][col] == -1:
                SCREEN.blit(O_PNG, (col * CELL_SIZE + 60, row * CELL_SIZE + 70))

    pygame.display.update()

pygame.quit()
sys.exit()

# Sources; 
# Baraltech, Youtube, ‘Make Tic Tac Toe in PYTHON and PYGAME’, https://www.youtube.com/watch?v=IL_PMGVxEUY
# Coder Space, Youtube, ‘Coding Tic Tac Toe in Python with Pygame’, https://www.youtube.com/watch?v=q_Nzuyvf3tw 
# Coding With Russ, Youtube, ‘Python Tic Tac Toe Beginner Tutorial in Pygame | PART 2’, https://www.youtube.com/watch?v=vpodgih0X0Q 
# Pygame Documentation, ‘2. Revision: Pygame fundamentals’, https://www.pygame.org/docs/tut/tom_games2.html#makegames-2-2 
# Pygame Documentation, ‘​​pygame.display’, https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode 

