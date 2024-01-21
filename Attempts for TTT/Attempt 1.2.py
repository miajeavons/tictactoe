import pygame 

pygame.init()
# window 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# making rectangle 
player = pygame.Rect((300,250,50,50))

# game loop - while loop 
run = True 
while run == True: 
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0), player)

    # controlls (left, right, up, down)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    

# event handler - only one your intrested in is the one that exits the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.update()

pygame.quit()