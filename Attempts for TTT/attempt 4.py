import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe!")
WIN_SIZE = 800
CELL_SIZE = WIN_SIZE // 3

click = False
current_pos = []
player = 1

BOARD = pygame.transform.scale(pygame.image.load("Board.png"), ([WIN_SIZE] * 2))
X_PNG = pygame.transform.scale(pygame.image.load("X.png"), ([CELL_SIZE] * 2))
O_PNG = pygame.transform.scale(pygame.image.load("O.png"), ([CELL_SIZE] * 2))

BG_COLOUR = (64, 110, 61)

graphical_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not click:
            click = True
        if event.type == pygame.MOUSEBUTTONUP and click:
            click = False
            current_pos = pygame.mouse.get_pos()
            cell_x = current_pos[0] // CELL_SIZE
            cell_y = current_pos[1] // CELL_SIZE
            if graphical_board[cell_y][cell_x] == 0:
                graphical_board[cell_y][cell_x] = player
                player *= -1

    SCREEN.fill(BG_COLOUR)
    SCREEN.blit(BOARD, (64, 64))

    for row in range(3):
        for col in range(3):
            if graphical_board[row][col] == 1:
                SCREEN.blit(X_PNG, (col * CELL_SIZE + 64, row * CELL_SIZE + 64))
            elif graphical_board[row][col] == -1:
                SCREEN.blit(O_PNG, (col * CELL_SIZE + 64, row * CELL_SIZE + 64))

    pygame.display.update()

pygame.quit()
sys.exit()