import pygame
import sys

class TicTacToeGame:
    def __init__(self):
        pygame.init()
        
# Section 1: board set up 
        self.WIDTH, self.HEIGHT = 600, 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe!")
        self.WIN_SIZE = 500
        self.CELL_SIZE = self.WIN_SIZE // 3
# font 
        self.font = pygame.font.Font(None, 32)

# variables for while loop
        self.click = False
        self.current_pos = []
        self.player = 1

# images Scaled 
# https://www.youtube.com/watch?v=IL_PMGVxEUY 
# I took the pygame.image.load function and scaled the image in reference to my window and cell size
        self.BOARD = pygame.transform.scale(pygame.image.load("Board.png"), ([self.WIN_SIZE] * 2))
        self.X_PNG = pygame.transform.scale(pygame.image.load("X.png"), ([self.CELL_SIZE] * 2))
        self.O_PNG = pygame.transform.scale(pygame.image.load("O.png"), ([self.CELL_SIZE] * 2))
        self.BG_COLOUR = (0, 0, 0)

# graphical board with no values
        self.graphical_board = [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]]

    def check_win(self): # win probabilities
        for i in range(3):
            if self.graphical_board[i][0] == self.graphical_board[i][1] == self.graphical_board[i][2] != 0:
                return True  # row win
            if self.graphical_board[0][i] == self.graphical_board[1][i] == self.graphical_board[2][i] != 0:
                return True  # column win
        if self.graphical_board[0][0] == self.graphical_board[1][1] == self.graphical_board[2][2] != 0:
            return True  # diagonal win
        if self.graphical_board[0][2] == self.graphical_board[1][1] == self.graphical_board[2][0] != 0:
            return True  # diagonal win
        return False

# event handler - exits the game
# https://www.youtube.com/watch?v=vpodgih0X0Q 
#  I took the position of the mouse being clicked by printed on the screen who wins as well as adapting the code into mine using CELL_SIZE instead of a numerical value. 
    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
# shows click can process the event
                if event.type == pygame.MOUSEBUTTONDOWN and not self.click:
                    self.click = True
# take position where mouse was clicked
                if event.type == pygame.MOUSEBUTTONUP and self.click:
                    self.click = False
                    self.current_pos = pygame.mouse.get_pos()
                    cell_x = self.current_pos[0] // self.CELL_SIZE
                    cell_y = self.current_pos[1] // self.CELL_SIZE

                    if self.graphical_board[cell_y][cell_x] == 0:
                        self.graphical_board[cell_y][cell_x] = self.player
                        self.player *= -1  # if player1 is originally 1, player2 would be -1

# prints who wins on the screen 
                    if self.check_win():
                        text = self.font.render(f"Player {1 if self.player == -1 else 2} wins!", True, (255, 87, 51))
                        self.SCREEN.blit(text, (240, 20))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        run = False

            self.SCREEN.fill(self.BG_COLOUR)
            self.SCREEN.blit(self.BOARD, (64, 64))

# adds the images of X and O
            for row in range(3):
                for col in range(3):
                    if self.graphical_board[row][col] == 1:
                        self.SCREEN.blit(self.X_PNG, (col * self.CELL_SIZE + 60, row * self.CELL_SIZE + 70))
                    elif self.graphical_board[row][col] == -1:
                        self.SCREEN.blit(self.O_PNG, (col * self.CELL_SIZE + 60, row * self.CELL_SIZE + 70))

            pygame.display.update()

        pygame.quit()
        sys.exit()

# due to having a class;
if __name__ == "__main__":
    game = TicTacToeGame()
    game.run_game()

# Sources; 
# Baraltech, Youtube, ‘Make Tic Tac Toe in PYTHON and PYGAME’, https://www.youtube.com/watch?v=IL_PMGVxEUY
# Coder Space, Youtube, ‘Coding Tic Tac Toe in Python with Pygame’, https://www.youtube.com/watch?v=q_Nzuyvf3tw 
# Coding With Russ, Youtube, ‘Python Tic Tac Toe Beginner Tutorial in Pygame | PART 2’, https://www.youtube.com/watch?v=vpodgih0X0Q 
# Pygame Documentation, ‘2. Revision: Pygame fundamentals’, https://www.pygame.org/docs/tut/tom_games2.html#makegames-2-2 
# Pygame Documentation, ‘​​pygame.display’, https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode 

