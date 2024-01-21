# Links used: https://github.com/baraltech/Tic-Tac-Toe/blob/main/main.py 
# https://www.google.com/search?q=how+to+code+tic+tac+toe+in+python+pygame&sca_esv=598377228&sxsrf=ACQVn09bWexby_6OmDUMZbpdo-gT8UpRRw%3A1705237033645&ei=KdqjZZ7iJqy39u8PqIWZ8A4&ved=0ahUKEwjempf99tyDAxWsm_0HHahCBu4Q4dUDCBA&uact=5&oq=how+to+code+tic+tac+toe+in+python+pygame&gs_lp=Egxnd3Mtd2l6LXNlcnAiKGhvdyB0byBjb2RlIHRpYyB0YWMgdG9lIGluIHB5dGhvbiBweWdhbWUyBRAhGJ8FMgUQIRifBUjODVCqA1jrC3ABeAGQAQCYAZQBoAHIBaoBAzUuMrgBA8gBAPgBAcICChAAGEcY1gQYsAPCAhMQLhiABBiKBRhDGMcBGNEDGLADwgIGEAAYFhgewgILEAAYgAQYigUYhgPCAgUQIRigAcICBxAhGAoYoAHiAwQYACBBiAYBkAYJ&sclient=gws-wiz-serp#kpvalbx=_MdqjZbLkDtmDhbIPqPqo6Aw_50 
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode 
# https://thepythoncode.com/article/make-a-tic-tac-toe-game-pygame-in-python 
# https://www.pygame.org/docs/tut/tom_games2.html#makegames-2-2 
import pygame 
import sys 
pygame.init()
 
    # setting up background/board
WIDTH,HEIGHT = 900, 900
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe!")
WIN_SIZE = 800 
CELL_SIZE = WIN_SIZE // 3

    # load images scaled
BOARD = pygame.transform.scale(pygame.image.load("Board.png"), ([WIN_SIZE] * 2 )) 
X_PNG = pygame.transform.scale(pygame.image.load("X.png"), ([CELL_SIZE] * 2)) 
O_PNG = pygame.transform.scale(pygame.image.load("O.png"), ([CELL_SIZE] * 2))

BG_COLOUR = (64, 110, 61)

graphical_board = [[[0, 0], [0, 1], [0, 1]], 
                    [[1, 0], [1, 1], [1, 2]], 
                    [[2, 0], [2, 1], [2, 2]]]


SCREEN.fill(BG_COLOUR)
SCREEN.blit(BOARD, (64, 64))
pygame.display.update()

run = True
while run :    
# event handler - exits the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: 
                # left click is X 
                pygame.transform.scale(pygame.image.load("X.png"), ([CELL_SIZE] * 2))
            elif pygame.mouse.get_pressed()[1]:
                pygame.transform.scale(pygame.image.load("O.png"), ([CELL_SIZE] * 2))
                # right click is O
pygame.display.update()
# its not working.

pygame.display.update()
pygame.quit()

