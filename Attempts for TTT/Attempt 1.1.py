# TIC-TAC-TOE
import pygame 
pygame.init()
import sys
from random import randint
# display mode  
pygame.display.set_mode((0, 0), 0, 0)

# create window 
WIN_SIZE = 900

CELL_SIZE = WIN_SIZE // 3 
# add display caption 
pygame.display.set_caption("Tic-Tac-Toe!")

INF = float('inf')


class TicTacToe: 
    def __init__(self, game):
    # setting up screen 
        self.game = game
        self.field_image = self.get_scaled_image(path='Board.png', res=[WIN_SIZE]* 2)
        self.X_image = self.get_scaled_image(path= 'X.png', res=[CELL_SIZE] * 2)
        self.O_image = self.get_scaled_image(path='O.png', res=[CELL_SIZE]* 2)

        self.game_array = [[[INF,INF],[INF,INF],[INF,INF]],
                        [[INF,INF],[INF,INF],[INF,INF]],
                        [[INF,INF],[INF,INF],[INF,INF]]]
        self.player = randint(0,1)

    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != INF:
                    self.game.screen.blit(self.X_image if obj else self.O_image)
    
    
    def draw(self):
        self.game.screen.blit(self.field_image,(0,0))   




# game loop - while loop 
run = True 
while run:    
# event handler - exits the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()

# why is there a black screen still :/