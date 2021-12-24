import pygame
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN

#initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Continuous Movement")

#set game values
VELOCITY = 1
keys=pygame.key.get_pressed()

#declare movement
move_up = False
move_down = False
move_right = False
move_left = False

#load in images
ezio_image = pygame.image.load("Ezio.png")
ezio_rect = ezio_image.get_rect()
ezio_rect.centerx = WINDOW_WIDTH//2
ezio_rect.top = 0

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_UP):
                move_up = True
            if(event.key == pygame.K_DOWN):
                move_down = True
            if(event.key == pygame.K_RIGHT):
                move_right = True
            if(event.key == pygame.K_LEFT):
                move_left = True

        elif (event.type == pygame.KEYUP):
            if(event.key == pygame.K_UP):
                move_up = False
            if(event.key == pygame.K_DOWN):
                move_down = False
            if(event.key == pygame.K_RIGHT):
                move_right = False
            if(event.key == pygame.K_LEFT):
                move_left = False
        if event.type == pygame.QUIT:
            running = False
   
    if (move_up == True):                       #to make sure there was an up movement
        if((ezio_rect.y - VELOCITY) >= 0):      #to make sure it doesn't go across window borders
            ezio_rect.y -= VELOCITY
    if (move_down == True):
        if((ezio_rect.y + VELOCITY) < (WINDOW_HEIGHT- 90)):     # -90 to avoid the problem of hiding the picture partially due to the specificity of get_rect 
            ezio_rect.y += VELOCITY
        elif((ezio_rect.y + VELOCITY) >= (WINDOW_HEIGHT- 90)):
            ezio_rect.y = WINDOW_HEIGHT - 90
    if (move_right == True):
        if ((ezio_rect.x + VELOCITY) < (WINDOW_WIDTH- 75)):
            ezio_rect.x += VELOCITY
        else:
            ezio_rect.x = WINDOW_WIDTH - 75
    if (move_left == True):
        if ((ezio_rect.x - VELOCITY) > 0):
            ezio_rect.x -= VELOCITY

        

    #Fill the display
    display_surface.fill((0, 0, 0))

    #blit image to display 
    display_surface.blit(ezio_image, ezio_rect)

    #update the display
    pygame.display.flip()

#end the game
pygame.quit()